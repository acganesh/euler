def num_letters(n):
	thousand = [len('onethousand')]
	hundreds = [len('onehundred'), len('twohundred'), len('threehundred'), len('fourhundred'), len('fivehundred'), len('sixhundred'), len('sevenhundred'), len('eighthundred'), len('ninehundred')]
	tens = [0, len('ten'), len('twenty'), len('thirty'), len('forty'), len('fifty'), len('sixty'), len('seventy'), len('eighty'), len('ninety')]
	teens = [len('ten'), len('eleven'), len('twelve'), len('thirteen'), len('fourteen'), len('fifteen'), len('sixteen'), len('seventeen'), len('eighteen'), len('nineteen')]
	ones = [0, len('one'), len('two'), len('three'), len('four'), len('five'), len('six'), len('seven'), len('eight'), len('nine')]

	my_list = list(str(n))
	my_length = len(my_list)

	if my_length == 1:
		return ones[int(my_list[0])]
	elif my_length == 2:
		if 10 <= n < 20:
			index = (n % 10)
			return teens[index]
		else:
			return (tens[int(my_list[0])] + ones[int(my_list[1])])
	elif my_length == 3:
		#print hundreds[int(my_list[0])-1]
		#print tens[int(my_list[1])-1]
		#print ones[int(my_list[2])-1]

		if (n % 100) == 0:
			and_val = 0
		else:
			and_val = 3

		if 10 <= (n % 100) < 20:
			index = ((n % 100) % 10)
			teens_val = teens[index]
			return hundreds[int(my_list[0])-1] + teens_val + and_val
		else:
			return (hundreds[int(my_list[0])-1] + tens[int(my_list[1])] + ones[int(my_list[2])]) + and_val
	elif my_length == 4:
		return thousand[0]

n = 1
total_num_letters = 0
while n <= 1000:
	total_num_letters += num_letters(n)
	n += 1

print total_num_letters

