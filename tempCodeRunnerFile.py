import serial
import time
# import ConvertFloat

line = list()

if __name__ == "__main__":
    #Take 4 bytes of data from response data and convert to Binary
    ser = serial.Serial(port = 'COM4', \
                        baudrate = 115200,\
                        parity = serial.PARITY_NONE,\
                        stopbits = serial.STOPBITS_ONE,\
                        bytesize = serial.EIGHTBITS,\
                        timeout = 0)
    while (True):
        ser.open()
        
        line = ser.readline()

        print(str(count) + str(': ') + chr(line) )
        count = count+1