#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

#from mqtt_config import PWM_GPIO

class ServoSkill:
    def __init__(self, pwm, frequency):
        self.frequency = frequency

        GPIO.setmode(GPIO.BOARD) #use physical pin numbering/ Board numerotation mode
        GPIO.setwarnings(False) #disable warnings
        GPIO.setup(pwm, GPIO.OUT) #set pin as output
        time.sleep(1)
        self.pwm = GPIO.PWM(pwm, frequency)
        time.sleep(1)
        #self.pwm.start(self.angle_to_percent(90))
        self.pwm.start(0)
        time.sleep(2)
        #self.middle() # starting with middle position

    def angle_to_percent(self, angle):
        if angle > 180 or angle < 0:
            return False
        else:
            start = 4
            end = 12.5
            ratio = (end - start) / 180

            angle_as_percent = angle * ratio
            duty_cycle = start + angle_as_percent
            self.pwm.ChangeDutyCycle(duty_cycle)
        return None

    def left(self):
        print("Turning left")
        self.angle_to_percent(60) #links
        time.sleep(1)
        self.angle_to_percent(90)
        time.sleep(1)
        print("finished skill left")

    def right(self):
        print("Turning right")
        self.angle_to_percent(120) #rechts
        time.sleep(1)
        self.angle_to_percent(90)
        time.sleep(1)
        print("finished skill right")

    def middle(self):
        print("Turning middle")
        self.angle_to_percent(90) #mitte
        time.sleep(1)
        print("finished skill middle")

    def close(self):
        #close GPIO & cleanup
        self.pwm.stop()
        time.sleep(1)
        GPIO.cleanup()