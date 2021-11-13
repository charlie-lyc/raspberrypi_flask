# encoding: utf-8

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


## Check Cron
# $ crontab -l

## Edit Cron
# $ crontab -e
## Code for executing every 1 minute
# * * * * * sudo python /home/pi/Documents/raspberrypi_flask/09_cron.py

# """한글이 포함되어 있을 경우"""에는 파일 최상단에 """ # encoding: utf-8 """"이 필요
# 또는
# * * * * * sudo python3 /home/pi/Documents/raspberrypi_flask/09_cron.py

## Examples for periodical execution
# *       *  *  *  * : every minute 
# 15,45   *  *  *  * : every 15 and 45 minute
# */10    *  *  *  * : with 10 minutes' intervals
# 0       2  *  *  * : at 2 am every day
# 30    */6  *  *  * : every 30 minute with six hours' intervals(00:30, 06:30, 12:30, 18:30)
# 30 1-23/6  *  *  * : every 30 minute with six hours' intervals from 1 am to 23 pm(01:30, 07:30, 13:30, 19:30)