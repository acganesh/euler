def main(M, limit):
	vals = [1]*(M)+[2,4]

	#Recursive solution: f(n) = f(n-1) + f(n-M) + f(n-5) + ...+ f(1) + f(0) + 1
	#Analogous to previous solution

	length = M+2
	val = 0
	while val < limit:
		val = vals[-1]+1
		for i in range(length-M):
			val += vals[i]
		vals.append(val)
		length += 1
	return length-1

print main(50, 10**6)