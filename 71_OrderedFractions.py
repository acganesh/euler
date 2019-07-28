from fractions import Fraction
def main(limit, frac):
	num = frac.numerator
	denom = frac.denominator
	d = 1.
	min_dist = 100 #arbitrary large number
	min_frac = None
	my_list = [frac]
	while d <= limit:
		n = round(num*d/denom)
		frac2 = Fraction(int(n),int(d))
		dist = frac - frac2
		if dist > 0 and dist < min_dist:
			min_dist = dist
			min_frac = frac2
		d += 1
	return min_frac
	

print main(10**6, Fraction(3,7))
