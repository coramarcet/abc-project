import RPi.GPIO as GPIO
from time import sleep

class move:
    def __init__(self):
        #pins for motor driver inputs 

        # left side
        Motor1A = 27
        Motor1B = 22
        Motor1E = 17
        #pwm1=GPIO.PWM(Motor1E, 1000) #PWM for left motor
        #pwm1.start(0) #start at 0% (off)

        # right side
        Motor2A = 26
        Motor2B = 13
        Motor2E = 19
        #pwm2=GPIO.PWM(11, 1000) #PWM for right motor
        #pwm2.start(0) #start at 0% (off)

    def stop():
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
     
    def setup():
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)
        GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)
        global pwm1
        pwm1 = GPIO.PWM(Motor1E, 1000)
        pwm1.start(0)
        global pwm2
        pwm2= GPIO.PWM(Motor2E, 1000)
        pwm2.start(0)
     
    #speed is an integer from 0-100 for the speed of the motor using PWM.

    def forward(speed):
        print("going forward")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        pwm1.ChangeDutyCycle(speed)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        pwm2.ChangeDutyCycle(speed)

    def backward(speed):
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        pwm1.ChangeDutyCycle(speed)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        pwm2.ChangeDutyCycle(speed)

    def right(speed):
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        pwm1.ChangeDutyCycle(speed)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        pwm2.ChangeDutyCycle(speed)

    def left(speed):
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        pwm1.ChangeDutyCycle(speed)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        pwm2.ChangeDutyCycle(speed)

    def turnAround():
        #180 degree turn and like back up kinda beat
        #we may need the GPS and compass to be able to do this and the other turning functions
        None

#uncomment for testing
# setup()
# print("running forward()")
# forward(100)
# sleep(10)
# stop()
# GPIO.cleanup()
