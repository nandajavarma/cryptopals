

def hex_to_bin(char):
    return bin(int(char, 16))[2:].zfill(4)

def hex_string_to_binary_string(hexstring):
    binary_string = ""
    for char in hexstring:
        binary_val = hex_to_bin(char)
        binary_string = binary_string + binary_val
    return binary_string.strip(" ")

# bin -> hex
def bin_to_hex(four_bytes):
    dec_num = int(four_bytes, 2)
    hex_num = hex(dec_num)[2:]
    return hex_num

def bin_string_to_hex_string(bin_string):
    result = ""
    while bin_string:
        eight_bytes = bin_string[:8]
        bin_string = bin_string[8:]
        result = result + bin_to_hex(eight_bytes)
    return result

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
