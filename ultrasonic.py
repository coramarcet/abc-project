#collect and report data collected by the HC-SR04 ultrasonic sensor
#source: https://github.com/Freenove/Freenove_RFID_Starter_Kit_for_Raspberry_Pi/blob/master/Tutorial.pdf
#tells user if it's about to run into anything

import RPi.GPIO as GPIO
import timefrom PCF8574 import PCF8574_GPIO
class ultrasonic:
    trig = 0 #Ultrasonic sensor trigger pin, WILL CHANGE IN __INIT__()
    echo = 0 #SAME AS ABOVE
    maximum = 220 # maximum distance (cm)
    timeOut = maximum*60 

    def __init__(self, trigPin, echoPin):
        trig = self.trigPin
        echo = self.echopPin
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
         t0 = time.time()
         while(GPIO.input(pin) != level):
         if((time.time() - t0) > timeOut*0.000001):
            return 0;
         t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        pulseTime = (time.time() - t0)*1000000
        return pulseTime

    def getSonar(): #get the measurement results of ultrasonic module,with unit: cm
        GPIO.output(trigPin,GPIO.HIGH) #make trigPin send 10us high level
        time.sleep(0.00001) #10us
        GPIO.output(trigPin,GPIO.LOW)
        pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut) #read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0
        return distance
