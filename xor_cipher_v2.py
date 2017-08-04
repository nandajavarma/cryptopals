import binascii
"""
We have: 

* a hex string
--> int from base 16

l: iterate ove ascii values ranging from 0 to 127(decimal by type) 
* xor ascii decimal and hex_to_dec value
* convert the result back to hex then to ascii
* if the ascii makes sense you're done

"""


def xor_hex_and_ascii(hexstring):
    ascii_dict = {}
    l = len(hexstring)
    decimal_val = int(hexstring, 16)
    for key in range(0, 127):
        b = int(("%x" % key) * l,16)
        xored_val = hex(decimal_val ^ key)[2:]
        the_ascii = binascii.unhexlify('0' * (len(xored_val) % 2) + xored_val)
        ascii_dict[key] = the_ascii
    return ascii_dict


if __name__ == '__main__':
    hex_str = "b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(xor_hex_and_ascii(hex_str))      
