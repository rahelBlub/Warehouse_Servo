#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

from mqtt_config import PWM_GPIO

class ServoSkill:
    def __init__(self, pwm, frequence):
        self.frequence = 50
        self.pwm = GPIO.PWM(PWM_GPIO, frequence)

        GPIO.setmode(GPIO.BOARD) #use physical pin numbering/ Board numerotation mode
        GPIO.setwarnings(False) #disable warnings
        GPIO.setup(PWM_GPIO, GPIO.OUT) #set pin as output

    def angle_to_percent(angle):
        if angle > 180 or angle < 0:
            return False

        start = 4
        end = 12.5
        ratio = (end - start) / 180

        angle_as_percent = angle * ratio
        return start + angle_as_percent

    def left(self):
        print("Turning left")
        self.pwm.start(angle_to_percent(70)) #links
        time.sleep(1)

    def right(self):
        print("Turning right")
        self.pwm.ChangeDutyCycle(angle_to_percent(120)) #rechts
        time.sleep(1)

    def close(self):
        #close GPIO & cleanup
        self.pwm.stop()
        GPIO.cleanup()