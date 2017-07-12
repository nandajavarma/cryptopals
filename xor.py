# 2x bin -> xor
from utils import bin_string_to_hex_string, hex_string_to_binary_string, xor




# main stuff
input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"
result = "746865206b696420646f6e277420706c6179"

def fixed_xor():
    bin_string1 = hex_string_to_binary_string(input1)
    bin_string2 = hex_string_to_binary_string(input2)
    xored_string = xor(bin_string1, bin_string2)
    hex_result = bin_string_to_hex_string(xored_string)
    return hex_result

if __name__ == "__main__":
    output = fixed_xor()
    print(output)
    assert output == result
