def series(*args):
	val = 0
	for item in args: val += 1./item
	return 1./val
	
def parallel(*args):
	return sum(args)

def string_split(string):
	split = []
	ctr = 1
	start_ind = 0
	while ctr < len(string):
		if string[ctr] != string[ctr-1]:
			split.append(string[start_ind:ctr])
			start_ind = ctr
		ctr += 1 
	split.append(string[start_ind:])
	return split

def capacitance_calculator(split, C):
	my_sum = 0
	for item in split:
		if 's' in item:
			my_sum += len(item)
		elif 'c' in item:
			my_sum += 1./len(item)
	return my_sum

def main(N):
	pass



print string_parser('ssrrs',1)

C = 1
#dummy variable for capacitance
N = 3


print series(60)
print parallel(60)
print series(60,60)
print parallel(60,60)

