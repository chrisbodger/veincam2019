import os
import threading
import time

import psutil  # To gain CPU stats of pi
import requests
from flask import Flask, render_template, request, Response, json

# DELETE: Check camera works: https://picamera.readthedocs.io/en/release-1.13/quickstart.html

# Horrible little hack for setting dev vs prod
if os.name == 'nt':
    DEBUG = True
    baseurl='http://localhost:8080'
    from camera_emulated import Camera
    import pigpio_emulated as io
    print('Dev mode')
else:
    DEBUG = False
    baseurl='http://10.0.0.5:8080'
    from camera_piopencv import Camera # Raspberry Pi camera module (requires picamera package)
    import pigpio as io
    print('Prod mode')

app = Flask(__name__)

# Set up some LED IO details and functions
# Note, the 3V 850nm LED group is on pin 21
LEDPinMap ={"850nm": {18},
            "940nm": {13},
            "Both": {13, 18},
            "Rail5V": {13, 18},
            }

pipin = io.pi()

def allLEDSOff():
    [pipin.write(pin,0) for pin in LEDPinMap['Both']]


# Flag to indicate whether user has loaded index or not
# Used to enable or disable LED blinking on first load of the app
had_index_requests = False

#---
# Caching.  Relies on the application only ever being accessed by one user (browser) at a
# time, which is quite specific and peculiar to this particular application.
# Saves having to use session variables and cookies etc.
# Should probably be converted to an object with methods at some point

# Settings cache
settings_cache = dict()
settings_file = os.path.join(app.static_folder, 'json/settings_custom.json')
#TODO - Use case where custom config is corrupt or does not exist.
settings_cache = json.load(open(settings_file))

# System stat cache
# For holding resource usage stats - reported in HTML
stats_cache = dict()

#---
# Index and AJAX service VIEWS
def updateSettingsCache(attr, val):
    # Update both the in-memory dict and the SD card savefile
    settings_cache[attr]=val
    with open(settings_file, 'w') as sf:
        json.dump(settings_cache, sf, sort_keys=True, indent=4)
    return

def updateSystemStats():
    stats_cache['cpu_usage']=round(psutil.cpu_percent())
    stats_cache['ram_usage']=round(psutil.virtual_memory().percent)
    # also... memavail=psutil.virtual_memory().available
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # print('{:,.1f}'.format(memavail/float(1<<20))+" MB")
    try: 
        ctemps = psutil.sensors_temperatures()
        stats_cache['cpu_temp']=round(ctemps['cpu-thermal'][0][1])
    except AttributeError as error:
        # Output expected AttributeErrors.
        print(error)
        stats_cache['cpu_temp']=round(0.05)
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)
        stats_cache['cpu_temp']=round(0.05)
    return


@app.route('/')
def index():
    #print(settings_cache)
    updateSystemStats() # Updates stats cache before first render

    # Update a global indicating index has been requested (will stop any LED blinking) 
    global had_index_requests
    if not had_index_requests:
        had_index_requests = True

    return render_template('index.html',
                           config_data=settings_cache,
                           stats_data=stats_cache)

# Execute server-side intent of client 'attribute' AJAX calls
def alterAppName(val):
    # 1 Alter running level
    # 2 Update hard coded json config
    # 3 return success code.
    updateSettingsCache('app_name',val)

def alterLightLevel(val):
    # Allows (and expects) one of 5 levels, for PWM
    # Also alters level depending on current wavelength (called by alterLightWavelength function)
    # https://www.quora.com/What-is-the-difference-between-duty-cycle-and-frequency
 
    if (val in (1,2,3,4,5)):
        # 1 Alter running level
        # # 2 Update hard coded json config
        # 3 return success code.
        duty_cycle = 250000*(val-1) # max is 1000000, val of 1 effectively sets only 3V lights on.
        # Only alters state of LEDs for given wavelength.
        # Deal with the LEDs for the given wavelength
        activeLEDs5V = LEDPinMap[settings_cache['light_wavelength']].intersection( LEDPinMap["Rail5V"] )
        [pipin.hardware_PWM(pin, 800, duty_cycle) for pin in activeLEDs5V] #800Hz, beyond perception.

        if (val != settings_cache['light_level']): 
            updateSettingsCache('light_level',val) 
    elif val==0:
        allLEDSOff()
        if (val != settings_cache['light_level']): 
            updateSettingsCache('light_level',val) 
    else:
        pass
        
def alterLightWavelength(val):
    # TODO - only allow if camera is on (stop battery use from invisible 940nm)

    # 1 Alter running level
    # 2 Update hard coded json config
    # 3 return success code.
    allLEDSOff() # Set a blank slate

    if (val in ["850nm", "Both", "940nm"]):
        updateSettingsCache('light_wavelength',val)
        alterLightLevel(settings_cache['light_level'])

def alterROI(val):
    # 1 Alter running level
    # 2 Update hard coded json config
    # 3 return success code.
    if (val in ["Off", "Small", "Large"]):
        updateSettingsCache('roi',val)
  

def alterCamState(val):
    # The value passed should be a boolean.
    # 1 Alter running level
    updateSettingsCache('cam_state',val)

    # Also turn lights on or off, based on state and cached wavelength
    """
    if (val):
        alterLightWavelength(settings_cache['light_wavelength'])
    else:
        allLEDSOff()
    """

    # 2 Update hard coded json config
    # NOT done for cam state.  On startup the camera should
    # always be off, as will the lights.

    # 3 return success code.
    return

def alterCamSetting(attr,val):
    # The value passed should be a boolean.
    # 1 Alter running level
    updateSettingsCache(attr,val)


def shutdownServer():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def shutdownPi():
    from subprocess import call
    call("sudo nohup shutdown -h now", shell=True)
    return json.dumps({'status':'Server pi down...'})
    
@app.route('/shutserver', methods=['POST'])
def shutserver():
    shutdownServer()
    return json.dumps({'status':'Server shutting down...'})

@app.route('/shutpi', methods=['POST'])
def shutpi():
    shutdownPi()
    return json.dumps({'status':'Pi shutting down...'})

@app.route('/alter-config', methods=['POST'])
def alterConfig():
    # Data posted as a form, even though wasn't in a form in the posting html
    # See https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
    # https://codehandbook.org/python-flask-jquery-ajax-post/
    attribute = request.form['attribute']
    value = request.form['value']
    print('>attribute ', attribute, '| value ', value)

    # TODO if elif else statement running alter code depending on attribute passed in 
    if attribute == 'camera_state':
        # https://stackoverflow.com/questions/10693630/how-to-pass-a-boolean-from-javascript-to-python
        value = request.form['value'] == 'true'
        alterCamState(value)
    elif attribute == 'cam_contrast':
        alterCamSetting('cam_contrast',value)
    elif attribute == 'cam_brightness':
        alterCamSetting('cam_brightness',value)
    elif attribute == 'cam_shutspeed':
        alterCamSetting('cam_shutspeed',value)
    elif attribute == 'light_level':
        value = int(request.form['value'])
        alterLightLevel(value)
    elif attribute == 'light_wavelength':
        alterLightWavelength(value)
    elif attribute == 'roi':
        alterROI(value)
    elif attribute == 'app_name':
        alterAppName(value)
        
    else:
        pass

    return json.dumps({'status':'OK'})


@app.route('/refresh-stats', methods=['POST'])
def refreshStats():
    updateSystemStats() # Dynamic update to pass back in AJAX
    print(stats_cache)
    # Merge on a status message to the resuls before passing through
    current_stats = {**{'status':'OK'}, **stats_cache}
    return json.dumps(current_stats)

#---
# The main event... Video stream
# See https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited,
# https://github.com/miguelgrinberg/flask-video-streaming


def gen(camera):

    while settings_cache['cam_state']:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed', defaults={'increment': 0})
@app.route('/video_feed/<int:increment>/')
def video_feed(increment):

    global settings_cache
    camera = Camera(settings_cache)
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')    


#---
# Hack! Set blinking LED at app startup to indicate things are ready - see code at end
# Inspired by https://networklore.com/start-task-with-flask/
@app.route('/check_blink_status', methods=['GET'])
def checkBlinkStatus():
    global had_index_requests # Boolean, True if no index requests yet.
    return json.dumps({"had_index_requests": had_index_requests})


if __name__ == '__main__':
    try:
        # turn ready LED on and start server
        pipin.write(4, 1)
        app.run(host='0.0.0.0', port='8080', debug=DEBUG, threaded=True)
    finally:
        # turn ready LED off
        pipin.write(4, 0)