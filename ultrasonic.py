#collect and report data collected by ultrasonic sensor

import RPi.GPIO as GPIO
import timefrom PCF8574 import PCF8574_GPIO
class ultrasonic:
    trig = 0
    echo = 0
    def __init__(self, trigPin, echoPin):
        trig = self.trigPin
        echo = self.echopPin