def tribonacci(n, mod):
	vals = [1,1,1]
	length = 3
	while length < n:
		vals.append(sum(vals[-3:]) % mod)
		length += 1
	return vals

print tribonacci(100, 27)
