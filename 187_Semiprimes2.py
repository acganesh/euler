from datetime import datetime

#start = datetime.datetime.now()

def factor_sieve(n):
	sieve = [False]*(n+1)
	total = [0]*(n+1)
	ctr = 0
	for x in range(2, n+1):
		if not(sieve[x]):
			for y in range(x, n+1, x):
				exp = 1
				num = y
				while num % x == 0:
					num //= x
					exp += 1
					total[y] += 1
				sieve[y] = True
		if total[x] == 2:
			ctr += 1
	return sieve, ctr
def main(limit):
	factors, my_ctr = factor_sieve(limit)
	return my_ctr
	'''
	for item in total:
		if item == 2:
			ctr += 1
	print my_ctr
	return ctr
	'''

st1 = datetime.now()
print main(10**8)
e1 = datetime.now()
print e1-st1


'''

a = factor_sieve(10**6)

st2= datetime.now()
b = main(10**6)
e2 = datetime.now()
print 't2', e2 - st2
'''

#print factor_sieve(10**7)
#print main(100000000)
#print datetime.datetime.now() - start