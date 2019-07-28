def digits(n):
	return len(str(n))

def main(n):
	digit_counter = 0
	i = 1

	while digit_counter < n-1:
		digit_counter += digits(i)
		i += 1
	print str(i)[0]

def main2(n):
	my_str = ''
	i = 1
	while (len(my_str) < n):
		my_str += str(i)
		#print my_str
		i += 1
	return my_str

my_str = main2(10000000)
prod = int(my_str[0])*int(my_str[9])*int(my_str[99])*int(my_str[999])*int(my_str[9999])*int(my_str[99999])*int(my_str[999999])
print prod

