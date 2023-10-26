import serial
import time
import json
from DataStructure import *

line = list()
count = 0

root_node = Node()

if __name__ == "__main__":
    #Take 4 bytes of data from response data and convert to Binary
    ser = serial.Serial(port = 'COM4', baudrate = 115200)
    while (True):   
        line = ser.readline().decode('utf-8')
        print(line)
    
        parts = line.split("_")
        NodeID = int(parts[0])
        SensorID = int(parts[1])
        value = float(parts[2])
        root_node.updateNode(NodeID,SensorID,value)
        print_node_details(root_node)
        
    ser.close()