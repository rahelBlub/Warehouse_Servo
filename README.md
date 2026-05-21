# Warehouse_Servo

connect the signal-PIN (yellow/orange) to PIN 12 (GPIO 18)

connect the Ground-PIN (black) to GND 

connect the VCC-PIN (red) to 5V - it is recommended to use an external power supply and not the 5V PIN from the Pi,
because the servo(s) will cause the voltage to fluctuate significantly, which is a bad situation for the Pi.

starting pigpio daemon on Pi with: sudo pigpiod

start the service with: python3 Warehouse_Servo.py