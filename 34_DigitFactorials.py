from math import factorial 

num = 3

limit = 1000000

total_sum = 0

while num < limit:
	my_list = list(str(num))
	my_list_int = [int(x) for x in my_list]

	my_sum = 0

	for item in my_list_int:
		my_sum += factorial(item)

	if my_sum == num:
		#print num
		total_sum += num

	num += 1

print total_sum