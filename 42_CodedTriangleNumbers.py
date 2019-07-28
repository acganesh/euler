from math import sqrt, floor
import csv

def is_triangle_number(num):
	floored_root = floor(sqrt(2*num))
	if num == (floored_root * (floored_root + 1)/2):
		return True
	else:
		return False


def word_alphabet_value(str):
	dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
	
	val = 0
	for char in list(str):
		val += dict[char]

	return val

#print word_alphabet_value("SKY")

num_triangular_words = 0

with open('42_data.txt', 'rb') as f:
	my_reader = csv.reader(f)
	for element in my_reader:
		for word in element:
			if is_triangle_number(word_alphabet_value(word)): num_triangular_words += 1

print num_triangular_words
