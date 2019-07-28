from itertools import permutations
#for p in permutations('cat'):
	#print p

def get_perms(num):
	my_str = sorted(str(num))
	perms = [''.join(p) for p in permutations(my_str)]
	return perms

def is_concat_product(n):
	num_str = str(n)
	my_str = ""

	##Case 1: the number is 1 digit
	start_num = int(num_str[0])

	n = 1
	while my_str in num_str:
		my_str += str(start_num*n)
		n += 1

		if my_str == num_str:
			return True

	##Case 2: the number is 2 digits
	start_num = int(num_str[:2])

	my_str = ""
	n = 1

	while my_str in num_str:
		my_str += str(start_num*n)
		n += 1

		if my_str == num_str:
			return True

	##Case 3: the number is 3 digits
	start_num = int(num_str[:3])

	my_str = ""
	n = 1

	while my_str in num_str:
		my_str += str(start_num*n)
		n += 1

		if my_str == num_str:
			return True

	##Case 4: the number is 4 digits
	start_num = int(num_str[:4])

	my_str = ""
	n = 1

	while my_str in num_str:
		my_str += str(start_num*n)
		n += 1

		if my_str == num_str:
			return True

	return False

my_max = 0

perms = get_perms(123456789)
for num in perms:
	if is_concat_product(num):
		#print num
		if num > my_max:
			my_max = num

print my_max





	

