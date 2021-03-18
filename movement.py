import RPi.GPIO as GPIO
from time import sleep
#import gps

# Pins for Motor Driver Inputs 

# left side
Motor1A = 17
Motor1B = 27
Motor1E = 22
#pwm1=GPIO.PWM(Motor1E, 1000) #PWM for left motor
#pwm1.start(0) #start at 0% (off)

# right side
Motor2A = 10
Motor2B = 9
Motor2E = 11
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
    #go forward
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    pwm2.ChangeDutyCycle(speed)

def backward(speed):
    #go backward
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


def right():
    #turn right
    None

def left():
    #turn left
    None

def turnAround():
    #180 degree turn and like back up kinda beat
    #we may need the GPS and compass to be able to do this and the other turning functions
    None
    
setup()
print("running forward()")
forward(30)
sleep(5)
stop()
GPIO.cleanup()
    
