def convertToInt(mantissa_str):
    power_count = -1
    mantissa_int = 0

    for i in mantissa_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
         
    return (mantissa_int + 1)

def ConvertByteToFloat(Return_data):
    # Convert string to list for Return_data
    values = Return_data.split(",")
    values = [value.strip() for value in values]
    # Convert value at index 5 to integer
    A = int(values[0])
    B = int(values[1])
    C = int(values[2])
    D = int(values[3])


    # Combine into a 32-bit result using bitwise operations
    result_32_form = (A << 24) | (B << 16) | (C << 8) | D
    result_32_form_bin = '{:032b}'.format(result_32_form)
    
    sign_bit = int(result_32_form_bin[0])
    exponent= int(result_32_form_bin[1 : 9], 2)
    mantissa_str = result_32_form_bin[9 : ]
    mantissa_int = convertToInt(mantissa_str)

    float_value = pow(-1, sign_bit) * mantissa_int * pow(2, exponent - 127)
    return float_value

#Take 4 bytes of data from response data and convert to Binary
Return_data = bytearray([5, 3, 4, 95, 192, 65, 154, 159, 187])
float_value = ConvertByteToFloat(Return_data)
print(float_value)

Return_data_str = ""
for i in Return_data:
    Return_data_str += str(int(i)) + "|"
print(Return_data_str, type(Return_data_str))









