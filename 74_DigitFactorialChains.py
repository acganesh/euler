from math import factorial
from datetime import datetime

start = datetime.now()

cache = [-1]*10000000

def digit_fact(n):
	val = cache[n]
	if val != -1:
		return val
	else:
		n = str(n)
		total = 0
		for d in n:
			total += factorial(int(d))
		cache[int(n)] = total
		return total

def df_chain(n):
	chain = []
	chain_set = set()
	length = 0
	while True:
		n = digit_fact(n)
		if n not in chain_set:
			chain.append(n)
			chain_set.add(n)
			length += 1
		else:
			break
	return length+1

def main(limit, num_terms):
	count = 0
	n = 1
	while n <= limit:
		if df_chain(n) == num_terms:
			count += 1
		n += 1
		#if n % 100000 == 0: print n
	return count

print main(10**6, 60)
print datetime.now() - start