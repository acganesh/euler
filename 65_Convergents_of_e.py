from fractions import Fraction

def get_vals(n):
	vals = [1,2]
	ctr = 2
	even_ctr = 2
	while ctr < n:
		if ctr % 3 == 1:
			vals.append(2*even_ctr)
			even_ctr += 1
			ctr += 1
		else:
			vals.append(1)
			ctr += 1

	return vals

def nth_convergent(n):
	ctr = 1
	vals = get_vals(n)
	result = vals[-1]
	while ctr < n:
		result = vals[-ctr-1] + Fraction(1, result)
		ctr += 1
		result
	return 1/result + 2

def sum_digits(n):
	return sum([int(x) for x in list(str(n))])

print sum_digits(nth_convergent(99).numerator)




