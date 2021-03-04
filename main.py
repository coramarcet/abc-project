#this is middleman

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
    GPIO.setup(trigPin, GPIO.OUT) # set trigPin to output mode
    GPIO.setup(echoPin, GPIO.IN) # set echoPin to input mode

def loop():
    while(True):
        distance = getSonar()
        #print ("The distance is : %.2f cm"%(distance))
        if distance < 25:
            right(50)
        else:
            forward(50)
        time.sleep(1)

def __name__ == '__main__': #program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
