def num_of_digits(n):
	return len(list(str(n)))

def fib(limit):
	i = 3
	sum = 2
	list = [1, 2]
	fib = 2
	while num_of_digits(fib) < limit:
		fib = list[-1] + list[-2]
		if fib % 2 == 0:
			sum += fib
		list.append(list[-1] + list[-2])
		i+= 1
	print fib
	print i
	#print list


fib(1000)