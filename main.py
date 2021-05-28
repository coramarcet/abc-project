from wormonastring import getSerial
from ultrasanic import sonic
from movement import move
import time

def setup():
    obj = getSerial() #pH object
    ultra = sonic() #ultrasonic sensor object
    distance = ultra.getSonar() #distance variable for ultrasonic sensor
    swim = move() #movement object

def run():
    while(True):
        #determines distance from nearest object
        distance = ultra.getSonar()
        while(distance < 20):
            swim.right(100)
            time.sleep(1)
            swim.stop()
            distance = ultra.getSonar()
        
        #once there is no object in way, moves forward
        swim.forward(100)

        #gets the pH and writes it to a separate file
        print(obj.getpH())
        
        time.sleep(1)

def __init__(): #program start from here
    run()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
__init__()

