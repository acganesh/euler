from fractions import Fraction

def find_common_digits(num1, num2):
	str1 = str(num1)
	str2 = str(num2)
	common_chars = []
	for char in str1:
		if char in str2:
			common_chars.append(char)
	return common_chars

def is_digit_cancelling(num1, num2):
	common_digits = find_common_digits(num1, num2)

	if common_digits == []:
		return False

	str1 = str(num1)
	str2 = str(num2)

	for item in common_digits:
		str1 = str1.replace(item, "")
		str2 = str2.replace(item, "")

	try:
		cancelled_num1 = float(str1)
		cancelled_num2 = float(str2)
	except ValueError:
		return False

	try:
		if float(num1)/(num2) == float(cancelled_num1)/float(cancelled_num2):
			return True
		else: 
			return False
	except ZeroDivisionError:
		return False

a_range = range(1,100)
b_range = range(1,100)

my_fracs = []

for a in a_range:
	for b in b_range:
		#print a,b
		if not (a % 10 == 0 and b % 10 == 0) and (a < b):
			if is_digit_cancelling(a, b) == True:
				my_fracs.append(Fraction(a,b))

prod = 1
for item in my_fracs:
	prod *= item

print prod
				