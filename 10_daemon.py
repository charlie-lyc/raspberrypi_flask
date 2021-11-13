#! /usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO


LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    num = 0
    while True: # LED blinks 5 times
        sleep(1)
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED, GPIO.LOW)
        num = num + 1
        if num == 5:
            GPIO.cleanup()
            break
except KeyboardInterrupt:
    GPIO.cleanup()


## Add to top of file
# - #! /usr/bin/env python
## OR
# - #! /usr/bin/env python3.7
#...

## Modify 'rc.local' file 
# sudo nano /etc/rc.local
# _IP=$(hostname -I) || true
# if [ "$_IP" ]; then
#   printf "My IP address is %s\n" "$_IP"
# fi
#   # Execution in background(&)
#   python /home/pi/Documents/raspberrypi_flask/10_daemon.py &
# exit 0

## This means 'ALAWYS EXECUTING' 10_daemon.py in background when boot computer

## Check execution
# $ sudo reboot
## LED is on at first time for checking GPIO, then execute.

