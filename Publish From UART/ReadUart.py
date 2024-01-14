import serial
import time
import json
from DataStructure import *

def AnalyzeData(line, data):
    parts = line.split("/")
    data['NodeID'] = parts[0]
    data['SensorID'] = parts[1]
    data['value'] = "{:.2f}".format(float(parts[2]))
    root_node.updateNode(data['NodeID'], data['SensorID'], data['value'])
    print_node_details(root_node)
