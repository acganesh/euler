#Old version.  You don't need to compute each chain until it reaches 89 or 1 -- you can just store where numbers end at.  
#See 92_SquareDigitChain.py for a more optimized approach.

import datetime

start = datetime.datetime.now()

def square_digit_chain(n):

	chain = [n]

	my_list_int = [int(x) for x in list(str(n))]

	my_sum = 0

	while not(my_sum == 1 or my_sum == 89):
		my_sum = 0

		for item in my_list_int:
			my_sum += item ** 2

		my_list_int = [int(x) for x in list(str(my_sum))]

		chain.append(my_sum)
	return chain

limit = 10000000


num = 1
num_of_89s = 0

while num <= limit:
	chain = square_digit_chain(num)
	if chain[-1] == 89:
		num_of_89s += 1
	num += 1
	if num % 1000000 == 0: print num

end = datetime.datetime.now()
print num_of_89s
print "Time elapsed: " + str(end-start)
