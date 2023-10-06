import serial
import time
import ConvertFloat

if __name__ == "__main__":
    #Take 4 bytes of data from response data and convert to Binary
    while (True):
        ser = serial.Serial('COM4', 115200)

        line = ser.readline().decode('utf-8').rstrip()

        ser.close()

        IDtemp = line.rstrip('[0123456789, ]')
        Return_data = line.strip(IDtemp + "[]")
        float_value = ConvertFloat.ConvertByteToFloat(Return_data)

        Return_data_str = ""
        for i in Return_data:
            Return_data_str += str(int(i)) + "|"
        print(Return_data_str, type(Return_data_str))

        time.sleep(1000)
