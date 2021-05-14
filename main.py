from wormonastring import getSerial
import time

def setup():
    None
#     GPIO.setmode(GPIO.BOARD) #numbers GPIOs by physical location
#     GPIO.setup(trigPin, GPIO.OUT) # set trigPin to output mode
#     GPIO.setup(echoPin, GPIO.IN) # set echoPin to input mode

def loop():
    while(True):
#         distance = getSonar()
#         print ("The distance is : %.2f cm"%(distance))
#         if distance < 25:
#             right(50)
#         else:
#             forward(50)
        
        obj = getSerial()
        print(obj.getpH())
        
        time.sleep(1)

def __init__(): #program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
__init__()
