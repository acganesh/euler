def digital_sum(n):
	my_list = list(str(n))
	my_list_int = [int(x) for x in my_list]

	return sum(my_list_int)


a_list = range(1, 101)
b_list = range(1, 101)

my_list = []

max_sum = 0

for a in a_list:
	for b in b_list:
		power = a**b
		#print power
		ds = digital_sum(power)
		#print ds
		if ds > max_sum:
			max_sum = ds
print max_sum

