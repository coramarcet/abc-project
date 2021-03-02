import RPi.GPIO as GPIO
from time import sleep
import gps

# Pins for Motor Driver Inputs 

# left side
Motor1A = 24
Motor1B = 23
Motor1E = 25
pwm1=GPIO.PWM(25, 1000) #PWM for left motor
pwm1.start(0) #start at 0% (off)

# right side
Motor2A = 10
Motor2B = 9
Motor2E = 11
pwm2=GPIO.PWM(11, 1000) #PWM for right motor
pwm2.start(0) #start at 0% (off)

def stop():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
 
def setup():
	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
 
#speed is an integer from 0-100 for the speed of the motor using PWM.

def forward(speed):
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

def turnAround():
    #180 degree turn and like back up kinda beat
    #we may need the GPS and compass to be able to do this and the other turning functions