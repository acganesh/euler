def char2val(char):
	dict = {'C': 100, 'D': 500, 'I': 1, 'M': 1000, 'L': 50, 'V': 5, 'X': 10}
	return dict[char]

def val2char(val):
	dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XL', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
	return dict[val]

def str2num(roman_str):
	subtractive = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
	subtractive_set = set(['CM', 'CD', 'XC', 'XL', 'IX', 'IV'])

	total = 0

	for substr in subtractive_set:
		if substr in roman_str:
			total += subtractive[substr]
			roman_str = roman_str.replace(substr, '')

	for char in roman_str:
		total += char2val(char)

	return total


def roman(n):
	roman_str = ""

	dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
	
	vals = sorted(dict.keys())[::-1]
	chars = [dict[key] for key in vals]


	ctr = 0
	item = vals[ctr]

	while n > 0:
		item = vals[ctr]
		while n >= item:
			n -= item
			char = chars[ctr]
			roman_str += char
		ctr += 1
		
	return roman_str

def parse():
	data = []
	with open('89_data.txt', 'rb') as f:
		for line in f:
			data.append(line.replace('\n',''))
	return data

def main():
	strings = parse()
	lengths = []
	optimal_lengths = []
	nums = []
	diffs = []
	for s in strings:
		length = len(s)
		lengths.append(length)
		num = str2num(s)
		nums.append(num)
		optimal_len = len(roman(num))
		optimal_lengths.append(optimal_len)
		diff = length - optimal_len
		diffs.append(diff)
	return sum(diffs)

print main()








