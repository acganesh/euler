def main(n):
	vals = [1,2,4,8]
	length = 4
	while length < n:
		val = vals[-1]+vals[-2]+vals[-3]+vals[-4]
		vals.append(val)
		length += 1
	return val

print main(50)