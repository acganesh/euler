my_sum = 0
n = 1
while n <= 1000:
	my_sum += ((n ** n) % (10 ** 10))
	n += 1

print (my_sum % (10 ** 10))