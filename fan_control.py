## RPi Fan Control v.0.1 2018-02-10
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","")
        temp = temp.replace("'C","")
        return (int(float(temp)))

def fan_start():
        GPIO.output(4,True)

def fan_stop():
        GPIO.output(4,False)

while True:
        if measure_temp() > 50:
                fan_start()
        else:
                fan_stop()
        time.sleep(1)
