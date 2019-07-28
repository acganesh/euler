a_list = range(2, 101)
b_list = range(2, 101)

nums = []

for a in a_list:
	for b in b_list:
		nums.append(a ** b)

print len(set(nums))
