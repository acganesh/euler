from decimal import Context, Decimal


squares = set([x**2 for x in range(100)])

def digit_expansion(n, prec):
	context = Context(prec = prec+2)
	sqrt = str(context.sqrt(n))
	total = 0
	#delete last two decimal places to avoid rounding infelicities
	for d in sqrt[:-2]:
		if d != '.':
			total += int(d)
	return total

def main(limit, prec):
	n = 2
	total = 0
	while n <= limit:
		if n not in squares:
			total += digit_expansion(n, prec)
		n += 1
	return total

print main(100, 100)
print digit_expansion(2, 100)



