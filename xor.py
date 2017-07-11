# hex -> bin
def hex_to_bin(char):
    return bin(int(char, 16))[2:].zfill(4)

def hex_string_to_binary_list(hexstring):
    binary_string = ""
    for char in hexstring:
        binary_val = hex_to_bin(char)
        binary_string = binary_string + binary_val
    return binary_string.strip(" ")

# 2x bin -> xor
def xor(bin_string1, bin_string2):
    result = ""
    for a, b in zip(bin_string1, bin_string2):
        a = int(a)
        b = int(b)
        if ( a or b ) and ( not ( a and b ) ):
            result = result + "1"
        else:
            result = result + "0"
    return result

# bin -> hex
def bin_to_hex(four_bytes):
    dec_num = int(four_bytes, 2)
    hex_num = hex(dec_num)[2:]
    return hex_num

def bin_string_to_hex_string(bin_string):
    result = ""
    while bin_string:
        four_bytes = bin_string[:4]
        bin_string = bin_string[4:]
        result = result + bin_to_hex(four_bytes)
    return result



# main stuff
input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"
result = "746865206b696420646f6e277420706c6179"

def fixed_xor():
    bin_string1 = hex_string_to_binary_list(input1)
    bin_string2 = hex_string_to_binary_list(input2)
    xored_string = xor(bin_string1, bin_string2)
    hex_result = bin_string_to_hex_string(xored_string)
    return hex_result

if __name__ == "__main__":
    output = fixed_xor()
    print(output)
    assert output == result
