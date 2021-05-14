import serial
import time

ser = serial.Serial('/dev/ttyACM0')

class getSerial:
    def __init__(self):
        ser.flushInput()
    
    def getpH(self):
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-1].decode("utf-8"))
        return(decoded_bytes)
    
# obj = getSerial()
# for i in range(100):
#     print(obj.getpH())
#     time.sleep(0.5)

