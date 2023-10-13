import serial
import time
import json
from ConvertFloat import *

line = list()
count = 0

if __name__ == "__main__":
    #Take 4 bytes of data from response data and convert to Binary
    ser = serial.Serial(port = 'COM4', baudrate = 115200)
    while (True):   
        line = ser.readline().decode('utf-8')

        print(line)

        start_index = line.find("[")
        end_index = line.find("]")
        if start_index != -1 and end_index != -1:
            tempStr = line[:start_index]  # Extract A
            IDtemp = line[start_index:end_index + 1]  

        Return_data = json.loads(IDtemp)

        float_value = ConvertByteToFloat(Return_data)
        
        print(f"{tempStr}: {float_value}")
        
    ser.close()