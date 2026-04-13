#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

from mqtt_config import PWM_GPIO

class ServoSkill:
    def __init__(self, pwm, frequency):
        self.frequency = frequency

        GPIO.setmode(GPIO.BOARD) #use physical pin numbering/ Board numerotation mode
        GPIO.setwarnings(False) #disable warnings
        GPIO.setup(PWM_GPIO, GPIO.OUT) #set pin as output

        self.pwm = GPIO.PWM(PWM_GPIO, frequency)

    def angle_to_percent(self, angle):
        if angle > 180 or angle < 0:
            return False

        start = 4
        end = 12.5
        ratio = (end - start) / 180

        angle_as_percent = angle * ratio
        return start + angle_as_percent

    def left(self):
        print("Turning left")
        self.pwm.start(self.angle_to_percent(70)) #links
        time.sleep(1)
        print("finished skill left")

    def right(self):
        print("Turning right")
        self.pwm.ChangeDutyCycle(self.angle_to_percent(120)) #rechts
        time.sleep(1)
        print("finished skill right")

    def middle(self):
        print("Turning middle")
        self.pwm.ChangeDutyCycle(self.angle_to_percent(90)) #mitte
        time.sleep(1)
        print("finished skill middle")

    def close(self):
        #close GPIO & cleanup
        self.pwm.stop()
        GPIO.cleanup()