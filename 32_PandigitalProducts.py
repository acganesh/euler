from itertools import permutations
#for p in permutations('cat'):
	#print p

def get_perms(num):
	my_str = sorted(str(num))
	perms = [''.join(p) for p in permutations(my_str)]
	return perms

def is_pandigital_product(num):
	my_str = str(num)
	length = len(my_str)

	div_max = length - 2
	div1_range = range(1, div_max)
	div2_range = range(1, div_max)

	for div1 in div1_range:
		for div2 in div2_range:
			if div1 < div2:
				factor1 = int(my_str[:div1])
				factor2 = int(my_str[div1:div2])
				product = int(my_str[div2:])
				if factor1 * factor2 == product:
					return product
	return False

perms = get_perms(123456789)

output_list = []
my_sum = 0
for item in perms:
	output = is_pandigital_product(item)
	if not output == False:
		if not output in output_list:
			output_list.append(output)
			my_sum += output

print my_sum