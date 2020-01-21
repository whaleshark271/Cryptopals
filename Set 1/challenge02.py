'''
The Cryptopals Crypto Challenges
Set 1/ Challenge 2
Fixed XOR
'''
import binascii

def hex_xor(hex1, hex2):
	byte1 = binascii.unhexlify(hex1)
	byte2 = binascii.unhexlify(hex2)
	byte_answer = bytes([a ^ b for a, b in zip(byte1,byte2)])
	return byte_answer.hex()

def main():
	hex1 = "1c0111001f010100061a024b53535009181c"
	hex2 = "686974207468652062756c6c277320657965"
	expected_answer = "746865206b696420646f6e277420706c6179"
	answer = hex_xor(hex1, hex2)
	print("Expected answer: " + expected_answer)
	print("Answer         : " + answer)

if __name__ == "__main__":
	main()
