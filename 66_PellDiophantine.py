from math import sqrt,floor
from decimal import Decimal, Context
from fractions import Fraction
import traceback
import sys


squares = set([x**2 for x in range(32)])

def check_sol(a, b, N):
	a = long(a)
	b = long(b)
	if a**2 - N*b**2 == 1: return True
	else: return False

#calculates the continued fraction representation of sqrt(N)
#really inefficient though, because it computes more than necessary for sum numbers
#re-implemented in fundamental_solution() method
def cont_frac(N):
	context = Context(prec = 1000)
	val = Decimal(context.sqrt(N))
	rep = [floor(val)]
	ctr = 1
	while ctr <= 1000:
		val = Decimal(context.divide(1,(context.subtract(val,Decimal(floor(val))))))
		rep.append(floor(val))
		ctr += 1
	return rep

def fundamental_solution(N):
	context = Context(prec = 1000)
	val = Decimal(context.sqrt(N))
	rep = [floor(val)]
	val = Decimal(context.divide(1,(context.subtract(val,Decimal(floor(val))))))
	rep.append(floor(val))
	ctr = 1

	h_base = [0, 1]
	k_base = [1, 0]

	h_1 = rep[0]*h_base[-1] + h_base[-2]
	k_1 = rep[0]*k_base[-1] + k_base[-2]

	if check_sol(h_1, k_1, N):
		return h_1, k_1

	h_2 = rep[1]*h_1 + h_base[-1]
	k_2 = rep[1]*k_1 + k_base[-1]

	if check_sol(h_2, k_2, N):
		return h_2, k_2

	H = [h_1,h_2]; K = [k_1,k_2]

	h = h_2; k = k_2

	ind = 3
	frac = Fraction(int(h), int(k))

	while not(check_sol(frac.numerator, frac.denominator, N)):
		
		val = Decimal(context.divide(1,(context.subtract(val,Decimal(floor(val))))))
		rep.append(floor(val))
		#val = rep[ind-1]
		h = long(long(floor(val))*H[-1] + H[-2])
		k = long(long(floor(val))*K[-1] + K[-2])

		frac = Fraction(long(h), long(k))

		H.append(frac.numerator)
		K.append(frac.denominator)
		ind += 1

	return h, k

limit = 1000
num = 2
max_x = 0
max_num = None

while num <= limit:
	try:
		if num not in squares:
			x = fundamental_solution(num)[0]
			#print num, x
			if x > max_x:
				max_x = x
				max_num = num
	except:
		print sys.exc_info()[0], traceback.print_tb(sys.exc_info()[2])
		print num,' failed'
		import time; time.sleep(5)
	num += 1

print max_num, max_x