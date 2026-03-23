#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

from mqtt_config import PWM_GPIO

def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start) / 180

    angle_as_percent = angle * ratio
    return start + angle_as_percent

GPIO.setmode(GPIO.BOARD) #use physical pin numbering/ Board numerotation mode
GPIO.setwarnings(False) #disable warnings

#use pin 12 for pwm signal
PWM_GPIO = 12
frequence = 50
GPIO.setup(PWM_GPIO, GPIO.OUT) #set pin as output
pwm = GPIO.PWM(PWM_GPIO, frequence) #create PWM instance with frequency

#init at 0°
pwm.start(angle_to_percent(0))
time.sleep(1)

#go at 90°
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

#close GPIO & cleanup
pwm.stop()
GPIO.cleanup()