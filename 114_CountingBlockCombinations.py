def main(n):
	vals = [1,1,1,2,4]	

	#Recursive solution: f(n) = f(n-1) + f(n-4) + f(n-5) + ...+ f(1) + f(0) + 1
	#Analogous to previous solution

	length = 5
	while length < n+1:
		val = vals[-1]+1
		for i in range(length-3):
			val += vals[i]
		vals.append(val)
		length += 1
	print vals
	return val

print main(50)