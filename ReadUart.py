import serial
import time
import ConvertFloat

line = list()
count = 0

if __name__ == "__main__":
    #Take 4 bytes of data from response data and convert to Binary
    ser = serial.Serial(port = 'COM3', \
                        baudrate = 115200,\
                        parity = serial.PARITY_NONE,\
                        stopbits = serial.STOPBITS_ONE,\
                        bytesize = serial.EIGHTBITS,\
                        timeout = 0)
    while (True):   
        line = ser.readline()


        IDtemp = line.rstrip('[0123456789, ]')
        Return_data = line.strip(IDtemp + "[]")
        float_value = ConvertFloat.ConvertByteToFloat(Return_data)

        Return_data_str = ""
        for i in Return_data:
            Return_data_str += str(int(i)) + "|"
        print(Return_data_str, type(Return_data_str))

        time.sleep(1000)

        
    ser.close()