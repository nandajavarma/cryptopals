#!/usr/bin/python3
from utils import hex_string_to_binary_string

base64_encoding = {}

def gen_base64_index():
    global base64_encoding
    input_string = "0 A 16 Q 32 g 48 w 1 B 17 R 33 h 49 x 2 C 18 S 34 i 50 y 3 D 19 T 35 j 51 z 4 E 20 U 36 k 52 0 5 F 21 V 37 l 53 1 6 G 22 W 38 m 54 2 7 H 23 X 39 n 55 3 8 I 24 Y 40 o 56 4 9 J 25 Z 41 p 57 5 10 K 26 a 42 q 58 6 11 L 27 b 43 r 59 7 12 M 28 c 44 s 60 8 13 N 29 d 45 t 61 9 14 O 30 e 46 u 62 + 15 P 31 f 47 v 63 /"
    base64_encoding = {}
    tokens = input_string.split(" ")
    while tokens:
        key = tokens.pop(0)
        val = tokens.pop(0)
        base64_encoding[key] = val

def binary_list_to_base64_string(bit_string):
    base64_string = ""
    while bit_string:
       sixbits = bit_string[0:6]
       base64_index = int(sixbits, 2)
       bit_string =  bit_string[6:]
       base64_encoded_char = base64_encoding.get(str(base64_index))
       if base64_encoded_char:
           base64_string = base64_string + base64_encoded_char
    return base64_string


if __name__=="__main__":
    gen_base64_index()
    hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    binary_string = hex_string_to_binary_string(hexstring)
    base64_encoded_string = binary_list_to_base64_string(binary_string)
    print(base64_encoded_string)
    assert base64_encoded_string == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
