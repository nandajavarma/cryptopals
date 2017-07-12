from utils import hex_string_to_binary_string, xor
import re

# function to find the character frequency. string ->  dict(letter:frequency)
def char_frequency(string):
    freq_dict = {}
    formatted_string = re.sub(r'\W*\d*\s*', '', string)
    for char in formatted_string:
        lcase_char = char.lower()
        if lcase_char in freq_dict:
            freq_dict[lcase_char] = freq_dict[lcase_char] + 1
        else:
            freq_dict[lcase_char] = 1
    return freq_dict


# function to call xor on the bin_string and the key
def xor_with_keys(string):
    bin_string = hex_string_to_binary_string(string)
    binslen = len(bin_string)/8
    key_dict = {}
    for key in range(127):
        bin_key = bin(key)[2:].zfill(8) * 8
        xored_string = xor(bin_string, bin_key)
        key_dict[dec_to_ascii(key)] = bin_to_ascii(xored_string)
    return key_dict

def bin_to_dec(binary):
    return int(binary, 2)

def dec_to_ascii(decimal):
    return chr(decimal)

# bin to decimal to ascii
def bin_to_ascii(bin_string):
    result = ""
    eight_bytes = bin_string[-8:]
    dec_val = bin_to_dec(eight_bytes)
    print(dec_val)
    char = dec_to_ascii(dec_val)
    print(char)
    while bin_string:
        eight_bytes = bin_string[:8]
        bin_string = bin_string[8:]
        dec_val = bin_to_dec(eight_bytes)

        char = dec_to_ascii(dec_val)

        result = result + char
    return result

# decimal ascii to char


test_string = "The Jargon File contains a bunch of definitions of the term ‘hacker’, most having to do with technical adeptness and a delight in solving problems and overcoming limits. If you want to know how to become a hacker, though, only two are really relevant.  There is a community, a shared culture, of expert programmers and networking wizards that traces its history back through decades to the first time-sharing minicomputers and the earliest ARPAnet experiments.  The members of this culture originated the term ‘hacker’. Hackers built the Internet. Hackers made the Unix operating system what it is today.  Hackers make the World Wide Web work. If you are part of this culture, if you have contributed to it and other people in it know who you are and call you a hacker, you're a hacker.  The hacker mind-set is not confined to this software-hacker culture.  There are people who apply the hacker attitude to other things, like electronics or music — actually, you can find it at the highest levels of any science or art.  Software hackers recognize these kindred spirits elsewhere and may call them ‘hackers’ too — and some claim that the hacker nature is really independent of the particular medium the hacker works in. But in the rest of this document we will focus on the skills and attitudes of software hackers, and the traditions of the shared culture that originated the term ‘hacker’.  There is another group of people who loudly call themselves hackers, but aren't. These are people (mainly adolescent males) who get a kick out of breaking into computers and phreaking the phone system. Real hackers call these people ‘crackers’ and want nothing to do with them. Real hackers mostly think crackers are lazy, irresponsible, and not very bright, and object that being able to break security doesn't make you a hacker any more than being able to hotwire cars makes you an automotive engineer. Unfortunately, many journalists and writers have been fooled into using the word ‘hacker’ to describe crackers; this irritates real hackers no end.  The basic difference is this: hackers build things, crackers break them.  If you want to be a hacker, keep reading. If you want to be a cracker, go read the alt.2600 newsgroup and get ready to do five to ten in the slammer after finding out you aren't as smart as you think you are. And that's all I'm going to say about crackers."
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
if __name__ == "__main__":
    # print(char_frequency(test_string))
    # print(xor_with_keys(hex_string))
    print(xor_with_keys(hex_string))

