import RPi.GPIO as GPIO
import time

class sonic:
    def __init__(self):
        #pin setup
        global trig
        global echo

        global max
        global timeOut
        
        trig = 16
        echo = 18

        max = 220
        timeOut = max * 60
        print("initialized")

    def pulseIn(self, pin, level, timeOut):
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

    def getSonar(self): #get the measurement results of ultrasonic module,with unit: cm
         GPIO.output(trig,GPIO.HIGH) #make trigPin send 10us high level
         time.sleep(0.00001) #10us
         GPIO.output(trig,GPIO.LOW)
         pingTime = pulseIn(echo,GPIO.HIGH,timeOut) #read plus time of echoPin
         distance = pingTime * 340.0 / 2.0 / 10000.0
         return distance

    def setup(self):
         print ('Program is starting...')
         GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
         GPIO.setup(trig, GPIO.OUT) # set trigPin to output mode
         GPIO.setup(echo, GPIO.IN) # set echoPin to input mode
    def loop(self):
         while(True):
             distance = self.getSonar()
             print ("The distance is : %.2f cm"%(distance))
             time.sleep(1)

if __name__ == '__main__': #program start from here
     obj = sonic()
     obj.setup()
     try:
         obj.loop()
     except KeyboardInterrupt:
         GPIO.cleanup() 

