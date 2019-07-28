n = 2
total_sum = 0

while n < 1000000:
	my_list = list(str(n))
	my_list_int = [int(x) for x in my_list]

	my_sum = 0
	for item in my_list_int:
		my_sum += item ** 5

	if n == my_sum:
		#print n
		total_sum += n

	n += 1

print total_sum