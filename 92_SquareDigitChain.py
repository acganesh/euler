#After solving, found this article: http://en.wikipedia.org/wiki/Happy_number
import datetime

start = datetime.datetime.now()
'''
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

	#print my_sum
'''

def square_digits(n):
	my_sum = 0
	for digit in str(n):
		my_sum += (int(digit) ** 2)
	return my_sum

	

#print square_digit_chain(44)

#print square_digit_chain(85)

limit = 10000000

chain_ends = [None] * (limit + 1) #True if end in 89, False otherwise
chain_ends[1] = False
chain_ends[89] = True

#square_digit_chain(1)

num = 1
num_of_89s = 0

while num <= limit:
	chain = [num]
	last_val = chain[-1]
	chain_end = chain_ends[last_val]

	while chain_end == None:
		chain.append(square_digits(last_val))
		last_val = chain[-1]
		chain_end = chain_ends[last_val]

	if chain_end: num_of_89s += 1

	for term in chain:
		chain_ends[term] = chain_end

	num += 1
	if num % 1000000 == 0: print num

end = datetime.datetime.now()
print num_of_89s
print "Time elapsed: " + str(end-start)
