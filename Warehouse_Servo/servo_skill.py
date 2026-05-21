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
        time.sleep(0.5)
        self.pwm.start(self.angle_to_percent(90))
        #self.pwm.start(0)
        time.sleep(0.5)

    def angle_to_percent(self, angle):
        if angle > 180 or angle < 0:
            return False
        else:
            start = 4
            end = 12.5
            ratio = (end - start) / 180
            angle_as_percent = angle * ratio
            duty_cycle = start + angle_as_percent

            #duty_cycle = (angle / 18) + 2.5 # Convert angle to duty cycle
            #return self.pwm.ChangeDutyCycle(duty_cycle)
            return duty_cycle

    def left(self):
        print("Turning left")
        self.pwm.ChangeDutyCycle(self.angle_to_percent(60))
        #self.angle_to_percent(60) #links
        time.sleep(1)
        self.pwm.ChangeDutyCycle(self.angle_to_percent(90))
        #self.angle_to_percent(90)
        time.sleep(1)
        print("finished skill left")

    def right(self):
        print("Turning right")
        self.pwm.ChangeDutyCycle(self.angle_to_percent(120))
        #self.angle_to_percent(120) #rechts
        time.sleep(1)
        self.pwm.ChangeDutyCycle(self.angle_to_percent(90))
        #self.angle_to_percent(90)
        time.sleep(1)
        print("finished skill right")

    def middle(self):
        print("Turning middle")
        self.pwm.ChangeDutyCycle(self.angle_to_percent(90))
        #self.angle_to_percent(90) #mitte
        time.sleep(1)
        print("finished skill middle")

    def close(self):
        #close GPIO & cleanup
        self.pwm.stop()
        GPIO.cleanup()