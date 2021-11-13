from flask import Flask
import RPi.GPIO as GPIO


app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def helloworld():
    return 'Hello World!'

## Request:
# /led/on
# /led/off
@app.route('/led/<state>')
def led(state):
    if state == 'on':
        GPIO.output(LED, GPIO.HIGH)
        return 'LED ON'
    elif state == 'off':
        GPIO.output(LED, GPIO.LOW)
        return 'LED OFF'

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return 'GPIO CLEANUP'


if __name__ == '__main__':
    app.run(host='0.0.0.0')