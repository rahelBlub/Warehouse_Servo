import pigpio
import time

class Skillset:
    def __init__(self, pwm):
        self.pi = pigpio.pi()
        time.sleep(1)
        self.pi.set_mode(pwm, pigpio.OUTPUT)

    def left(self):
        print("Turning left")
        self.pi.set_servo_pulsewidth(18, 1000)
        time.sleep(0.5)
        self.pi.set_servo_pulsewidth(18, 1500)
        time.sleep(0.5)
        print("finished skill left")

    def right(self):
        print("Turning right")

        print("finished skill right")

    def middle(self):
        print("Turning middle")

        print("finished skill middle")

    def close(self):
        # switch servo off
        self.pi.set_servo_pulsewidth(18, 0)
        self.pi.stop()
