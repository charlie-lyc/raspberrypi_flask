from flask import Flask, request
import RPi.GPIO as GPIO


app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def helloworld():
    return 'Hello World!'

## Request:
# /led
# /led?
@app.route('/led')
def led():
    # state = request.args.get('state', 'error')
    state = request.values.get('state', 'error')
    if state == 'on':
        GPIO.output(LED, GPIO.HIGH)
        return 'LED {}'.format(state.upper())
    elif state == 'off':
        GPIO.output(LED, GPIO.LOW)
        return 'LED {}'.format(state.upper())
    elif state == 'error': # Error handling
        return 'Query String Needed!'
    else:
        return 'Bad Request!'
    
@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return 'GPIO CLEANUP'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
