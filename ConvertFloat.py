def convertToInt(mantissa_str):
    power_count = -1
    mantissa_int = 0

    for i in mantissa_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
         
    return (mantissa_int + 1)

def ConvertByteToFloat(Return_data):
    
    # Convert value at index 5 to integer
    A = int(Return_data[2])
    B = int(Return_data[3])
    C = int(Return_data[0])
    D = int(Return_data[1])

    # Combine into a 32-bit result using bitwise operations
    result_32_form = (A << 24) | (B << 16) | (C << 8) | D
    result_32_form_bin = '{:032b}'.format(result_32_form)
    
    sign_bit = int(result_32_form_bin[0])
    exponent= int(result_32_form_bin[1 : 9], 2)
    mantissa_str = result_32_form_bin[9 : ]
    mantissa_int = convertToInt(mantissa_str)

    float_value = pow(-1, sign_bit) * mantissa_int * pow(2, exponent - 127)
    return round(float_value,2)











