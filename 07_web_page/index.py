from flask import Flask, request, render_template
import RPi.GPIO as GPIO


app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/led/on')
def led_on():
    try:
        GPIO.output(LED, GPIO.HIGH)
        return 'on'
    except Exception as identifier:
        return 'fail'

@app.route('/led/off')
def led_off():
    try:
        GPIO.output(LED, GPIO.LOW)
        return 'off'
    except Exception as identifier:
        return 'fail'


if __name__ == '__main__':
    app.run(host='0.0.0.0')