def digit_sum(n):
	my_list = list(str(n))
	my_list_int = [int(x) for x in my_list]
	return sum(my_list_int)

print digit_sum(2 ** 1000)