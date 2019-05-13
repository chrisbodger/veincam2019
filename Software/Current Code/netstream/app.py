# Import Libraries
import os

import psutil
from flask import Flask, render_template, request, Response, json

from camera_piopencv import Camera
import pigpio as io

DEBUG = False
baseurl='http://10.0.0.5:8080'
app = Flask(__name__)
LEDPinMap = {"850nm": {18},
             "940nm": {13},
             "Both": {13, 18},
             "Rail5V": {13, 18},
             }
pipin = io.pi()


def allLEDSOff():
    [pipin.write(pin, 0) for pin in LEDPinMap['Both']]


# Creates Settings Cache
settings_file = os.path.join(app.static_folder, 'json/settings_custom.json')
settings_cache = json.load(open(settings_file))

# Creates System Statistics Cache
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
    try: 
        ctemps = psutil.sensors_temperatures()
        stats_cache['cpu_temp'] = round(ctemps['cpu-thermal'][0][1])
    except AttributeError as error:
        # Output Expected AttributeErrors.
        print(error)
        stats_cache['cpu_temp'] = round(0.05)
    except Exception as exception:
        # Output Unexpected Exceptions.
        print(exception, False)
        stats_cache['cpu_temp'] = round(0.05)
    return


@app.route('/')
def index():
    updateSystemStats()
    return render_template('index.html', config_data=settings_cache, stats_data=stats_cache)


def alterAppName(val):
    updateSettingsCache('app_name',val)


def alterLightLevel(val):
    if val in (1, 2, 3):
        duty_cycle = 333333*val  # Max = 1000000
        activeLEDs5V = LEDPinMap[settings_cache['light_wavelength']].intersection(LEDPinMap["Rail5V"])
        [pipin.hardware_PWM(pin, 750, duty_cycle) for pin in activeLEDs5V]
        if val != settings_cache['light_level']:
            updateSettingsCache('light_level', val)
    elif val == 0:
        allLEDSOff()
        if val != settings_cache['light_level']:
            updateSettingsCache('light_level', val)
    else:
        pass


def alterLightWavelength(val):
    allLEDSOff()
    if val in ["850nm", "Both", "940nm"]:
        updateSettingsCache('light_wavelength',val)
        alterLightLevel(settings_cache['light_level'])


def alterROI(val):
    if val in ["Off", "Small", "Large"]:
        updateSettingsCache('roi', val)


def alterCamState(val):
    updateSettingsCache('cam_state', val)
    return


def alterCamSetting(attr, val):
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
    attribute = request.form['attribute']
    value = request.form['value']
    print('>attribute ', attribute, '| value ', value)

    if attribute == 'camera_state':
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
    elif attribute == 'state':
        alterCamSetting(attribute, value)
    elif attribute == 'color':
        alterCamSetting(attribute, value)
    else:
        pass
    return json.dumps({'status': 'OK'})


@app.route('/refresh-stats', methods=['POST'])
def refreshStats():
    updateSystemStats()
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
        # Turn Ready LED On and Start Server
        pipin.write(4, 1)
        app.run(host='0.0.0.0', port='8080', debug=DEBUG, threaded=True)
    finally:
        # Turn Ready LED Off
        pipin.write(4, 0)
