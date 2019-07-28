from fractions import Fraction
def sqrt_expansion(n):
	ctr = 0
	val = Fraction(2, 1)
	while ctr <= n-1:
		val = Fraction(2,1) + Fraction(1,1)/(val)
		ctr += 1.0
	return val - Fraction(1,1)

def more_digits_in_num(frac):
	if len(str(frac.numerator)) > len(str(frac.denominator)):
		return True
	else:
		return False

#print more_digits_in_num(Fraction(20, 3))
num = 1
limit = 1000

num_fractions = 0

while num <= limit:
	frac = sqrt_expansion(num)
	if more_digits_in_num(sqrt_expansion(num)):
		num_fractions += 1
		#print num
		#print frac
		#print num_fractions
	num += 1
	#if num % 100 == 0: print "Number of iterations %i" % num
print "Final number of successful fractions: %i" % num_fractions