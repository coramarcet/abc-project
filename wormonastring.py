# Gets the serial data from the arduino, which is the pH value.
# The arduino is the worm, and connected to a wire (string) to the RPi.

import serial
import time

ser = serial.Serial('/dev/ttyACM0')

class getSerial:
    def __init__(self):
        ser.flushInput()
    
    def getpH(self):
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-1].decode("utf-8"))
        
        text_file = open("data.txt", "w")
        line = []
        line += pH
        text_files.writelines(line)
        text_file.close()
        time.sleep(0.5)
        
        return(decoded_bytes)
