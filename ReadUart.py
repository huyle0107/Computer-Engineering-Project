import serial
import time
import json
from DataStructure import *

# if __name__ == "__main__":
#     #Take 4 bytes of data from response data and convert to Binary
#     ser = serial.Serial(port = 'COM4', baudrate = 115200)
#     while (True):   
#         line = ser.readline().decode('utf-8')
#         print(line)

def AnalyzeData(line, data):
    parts = line.split("_")
    data['NodeID'] = parts[0]
    data['SensorID'] = parts[1]
    data['value'] = float(parts[2])
    data['value'] = root_node.updateNode(data['NodeID'], data['SensorID'], data['value'])
    print_node_details(root_node)
