'''
The Cryptopals Crypto Challenges
Set 1/ Challenge 1
Convert hex to base64
'''
from binascii import unhexlify, b2a_base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

answer = b2a_base64(unhexlify(hex_string))

print("Expected answer: " + expected_answer)
print("Answer       : " + str(answer))
