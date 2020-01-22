'''
The Cryptopals Crypto Challenges
Set 1/ Challenge 4
Detect single-character XOR
'''
import binascii
import challenge03
from operator import itemgetter

def get_lines(filename):
	with open(filename) as f:
		content = f.read()
		hex_strings = content.splitlines()
	return hex_strings

def get_score(hex1):
	answer = ""
	best_score = 0
	score = 0
	for key in range(0xff):
		hex2 = str(key) * 30
		xor_string = challenge03.hex_xor(hex1, hex2)
		score = challenge03.scoring(xor_string)
		if score > best_score:
			best_score = score
			answer = xor_string
	return (best_score, answer)

def main():
	hex_strings = get_lines('challenge04.txt')
	scored_strings = [get_score(hex_strings[index]) for index in range(327)]
	best_answer = max(scored_strings, key=itemgetter(0))[1]
	print(best_answer)

if __name__ == "__main__":
	main()
