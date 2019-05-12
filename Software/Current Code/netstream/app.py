import os
import threading
import time

import psutil
import requests
from flask import Flask, render_template, request, Response, json

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
    from camera_piopencv import Camera
    import pigpio as io
    print('Prod mode')

app = Flask(__name__)

LEDPinMap = {"850nm": {18},
             "940nm": {13},
             "Both": {13, 18},
             "Rail5V": {13, 18},
             }

pipin = io.pi()


def allLEDSOff():
    [pipin.write(pin, 0) for pin in LEDPinMap['Both']]


had_index_requests = False

# Settings cache
settings_cache = dict()
settings_file = os.path.join(app.static_folder, 'json/settings_custom.json')
# TODO - Use case where custom config is corrupt or does not exist.
settings_cache = json.load(open(settings_file))  # !!!

# System stat cache
# For holding resource usage stats - reported in HTML
stats_cache = dict()


def updateSettingsCache(attr, val):
    # Update both the in-memory dict and the SD card savefile
    settings_cache[attr] = val
    with open(settings_file, 'w') as sf:
        json.dump(settings_cache, sf, sort_keys=True, indent=4)
    return


def updateSystemStats():
    stats_cache['cpu_usage'] = round(psutil.cpu_percent())
    stats_cache['ram_usage'] = round(psutil.virtual_memory().percent)
    # also... memavail=psutil.virtual_memory().available
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # print('{:,.1f}'.format(memavail/float(1<<20))+" MB")
    try: 
        ctemps = psutil.sensors_temperatures()
        stats_cache['cpu_temp'] = round(ctemps['cpu-thermal'][0][1])
    except AttributeError as error:
        # Output expected AttributeErrors.
        print(error)
        stats_cache['cpu_temp'] = round(0.05)
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)
        stats_cache['cpu_temp'] = round(0.05)
    return


@app.route('/')
def index():
    updateSystemStats()  # Updates stats cache before first render
    # Update a global indicating index has been requested (will stop any LED blinking) 
    global had_index_requests
    if not had_index_requests:
        had_index_requests = True
    return render_template('index.html', config_data=settings_cache, stats_data=stats_cache)


# Execute server-side intent of client 'attribute' AJAX calls
def alterAppName(val):
    updateSettingsCache('app_name',val)


def alterLightLevel(val):
    if (val in (1,2,3,4,5)):
        duty_cycle = 250000*(val - 1)
        # max is 1000000, val of 1 effectively sets only 3V lights on.
        # Only alters state of LEDs for given wavelength.
        # Deal with the LEDs for the given wavelength
        activeLEDs5V = LEDPinMap[settings_cache['light_wavelength']].intersection( LEDPinMap["Rail5V"] )
        [pipin.hardware_PWM(pin, 800, duty_cycle) for pin in activeLEDs5V]  # 800Hz, beyond perception.

        if val != settings_cache['light_level']:
            updateSettingsCache('light_level', val)
    elif val == 0:
        allLEDSOff()
        if val != settings_cache['light_level']:
            updateSettingsCache('light_level', val)
    else:
        pass


def alterLightWavelength(val):
    # TODO - only allow if camera is on (stop battery use from invisible 940nm)

    allLEDSOff()

    if (val in ["850nm", "Both", "940nm"]):
        updateSettingsCache('light_wavelength',val)
        alterLightLevel(settings_cache['light_level'])


def alterROI(val):

    if val in ["Off", "Small", "Large"]:
        updateSettingsCache('roi', val)
  

def alterCamState(val):
    updateSettingsCache('cam_state', val)
    return


def alterCamSetting(attr, val):
    # The value passed should be a boolean.
    # 1 Alter running level
    updateSettingsCache(attr, val)


def shutdownServer():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def shutdownPi():
    from subprocess import call
    call("sudo nohup shutdown -h now", shell=True)
    return json.dumps({'status': 'Server pi down...'})


@app.route('/shutserver', methods=['POST'])
def shutserver():
    shutdownServer()
    return json.dumps({'status': 'Server shutting down...'})


@app.route('/shutpi', methods=['POST'])
def shutpi():
    shutdownPi()
    return json.dumps({'status': 'Pi shutting down...'})


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
        alterCamSetting('cam_contrast', value)
    elif attribute == 'cam_brightness':
        alterCamSetting('cam_brightness', value)
    elif attribute == 'cam_shutspeed':
        alterCamSetting('cam_shutspeed', value)
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
    return json.dumps({'status': 'OK'})


@app.route('/refresh-stats', methods=['POST'])
def refreshStats():
    updateSystemStats()  # Dynamic update to pass back in AJAX
    print(stats_cache)
    current_stats = {**{'status':'OK'}, **stats_cache}
    return json.dumps(current_stats)


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


if __name__ == '__main__':
    try:
        # turn ready LED on and start server
        pipin.write(4, 1)
        app.run(host='0.0.0.0', port='8080', debug=DEBUG, threaded=True)
    finally:
        # turn ready LED off
        pipin.write(4, 0)