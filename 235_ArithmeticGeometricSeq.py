from decimal import Context, Decimal
context = Context(prec = 15)

target = -600000000000
tol = 100000
def u(k,r):
	r = Decimal(r)
	return context.multiply(900-3*k,r**(k-1))

def s(n, r):
	total = 0
	k = 1
	while k <= n:
		total += u(k, r)
		k += 1
	return total

r = 1.002322108632
while r <= 1.002322108633:
	val = s(5000, r)
	print "%.13f, %.13f, %r" % (val, r, val > target)
	r += 0.0000000000001

#After iterating through the values, manually found
#1.002322108633

#You should binary search instead -- see 235_ArithmeticGeometricSeq(online_sol) for the alg.


