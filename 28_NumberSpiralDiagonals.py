size = 3
my_sum = 1

ctr = 0

last_num = 1

dim = 1001

while size <= dim:
	ctr = 0
	while ctr < 4:
		last_num = last_num + (size - 1)
		my_sum += last_num

		ctr += 1
	size += 2

print my_sum


