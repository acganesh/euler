def num_digits(n):
	return len(str(n))

base = 2
power = 1
result = base ** power

'''
n = 1
while True:
	if num_digits(2 ** n) > n:
		print n
		break
	n += 1
	if n % 10 == 0: print n
'''

nums = []
while power <= 1000:
	base = 1
	while num_digits(result) <= power:
		result = base ** power
		if num_digits(result) == power:
			nums.append(result)
		base += 1
	power += 1

print nums
print len(nums)