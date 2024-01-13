import serial
import time

ser = serial.Serial(port = 'COM3', baudrate = 115200)

import re

# def extract_number(text):
#   """
#   Extracts the first integer between 1 and 1000 from a string passed as a parameter.

#   Args:
#     text: The string to search for the number.

#   Returns:
#     The integer between 1 and 1000 found in the string, or None if no such number is found.
#   """
#   match = re.search(r"\d{1,3}", text)
#   if match:
#     number = int(match.group(0))
#     if 0 <= number <= 1000:
#       return number
#   return -28






while True:
    line = ser.readline().decode('utf-8')
    print(line)
