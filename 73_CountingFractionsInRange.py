from fractions import Fraction
from datetime import datetime
start = datetime.now()

def main(limit, frac1, frac2):
	num1 = frac1.numerator
	denom1 = frac1.denominator
	num2 = frac2.numerator
	denom2 = frac2.denominator

	my_list = set([])
	ctr = 0
	num_vals = 0

	d= 1
	while d <= limit:
		frac = frac1
		up_one = None
		n = num1*d/denom1
		while True:
			frac = Fraction(int(n+1), int(d))

			if frac1 < frac < frac2:
				if not frac in my_list:
					my_list.add(frac)
					num_vals += 1
			else: break
			n += 1
			ctr += 1
			if ctr % 1000000 == 0:
				print ctr
		d += 1

	return num_vals

print main(12000, Fraction(1,3), Fraction(1,2))
print datetime.now() - start
