'''
The Cryptopals Crypto Challenges
Set 1/ Challenge 3
Single-byte XOR cipher
'''
import binascii

# From http://www.data-compression.com/english.html
# It is good to have the frequency of the space character
chr_frequency = {
	'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
	'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
	'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
	'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def scoring(byte_string):
	score = 0
	for byte in byte_string:
		score += chr_frequency.get(chr(byte).lower(), 0)
	return score

def hex_xor(hex1, hex2):
	byte1 = binascii.unhexlify(hex1)
	byte2 = binascii.unhexlify(hex2)
	byte_answer = bytes([a ^ b for a, b in zip(byte1,byte2)])
	return byte_answer

def main():
	hex1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	answer = ""
	best_key = 0x00
	best_score = 0
	score = 0
	for key in range(0xff):
		hex2 = str(key) * 34
		xor_string = hex_xor(hex1, hex2)
		score = scoring(xor_string)
		if score > best_score:
			best_key = key
			best_score = score
			answer = xor_string
	print(chr(best_key) + ": " + str(answer))

if __name__ == "__main__":
	main()
