def sgn(N):
	if N == abs(N):
		return 1
	else:
		return 0

def is_Cardano(a,b,c):
	tol = 1e-8

	val1 = a+b*c**(1./2)
	val2 = a-b*c**(1./2)

	if sgn(val2) == 1:
		val = val1**(1./3) + val2**(1./3)
	else:
		val = val1**(1./3) - (-1*val2)**(1./3)

	if abs(1-val) < tol:
		return True
	else:
		return False

def main(limit):
	ctr = 1
	for a in range(1, limit+1):
		for b in range(1, limit-a+1):
			for c in range(1, limit-a-b+1):
				if is_Cardano(a,b,c):
					ctr += 1
	return ctr

print is_Cardano(2,1,5)
print main(1000)