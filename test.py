import serial
import time

ser = serial.Serial(port = 'COM11', baudrate = 115200)

while True:
    line = ser.readline()

    print("Client is running...", line)


    time.sleep(1)