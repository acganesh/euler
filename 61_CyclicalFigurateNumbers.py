import itertools

def is_cyclic(a, b):
	a = str(a); b = str(b)
	if a[-2:] == b[:2]:
		return True
	else:
		return False

def are_cyclic(vals):
	for a, b in itertools.izip(vals, vals[1:]+[vals[0]]):
		a = str(a)
		b = str(b)
		if a[-2:] != b[:2]:
			return False
	return True

def pent_nums(n):
	my_list = [m*(3*m-1)/2 for m in range(1, n+1)]
	return my_list

def square_nums(n):
	my_list = [m**2 for m in range(1, n+1)]
	return my_list

def tri_nums(n):
	my_list = [m*(m+1)/2 for m in range(1, n+1)]
	return my_list

def pent_dict(n):
	d = {}
	for m in range(1, n+1):
		val = m*(3*m-1)/2
		key = str(val)[:2]
		d.setdefault(key,[]).append(val)
	return d

def tri_dict(n):
	d = {}
	for m in range(1, n+1):
		val = m*(m+1)/2
		key = str(val)[:2]
		d.setdefault(key,[]).append(val)
	return d

def square_dict(n):
	d = {}
	for m in range(1, n+1):
		val = m**2
		key = str(val)[:2]
		d.setdefault(key,[]).append(val)
	return d

def f(key, *args):
	keys = []
	for d in args:
		try:
			vals = d[key]
			keys.append()


n = 200

pents = pent_dict(n)
pent_vals = pent_nums(n)
tris = tri_dict(n)
squares = square_dict(n)

for val1 in pent_vals:
	key1 = str(val1)[-2:]
	for val2 in squares[key1]:
		key2 = str(val2)[-2:]
		for val3 in tris[key2]:
			print val1, val2, val3

	for val2 in tris[key1]:
		key2 = str(val2)[-2:]
		for val3 in tris[key2]:
			print val1, val2, val3


'''
def is_triangle_number(num):
	floored_root = floor(sqrt(2*num))
	if num == (floored_root * (floored_root + 1)/2):
		return True
	else:
		return False

def is_hexagonal_number(num):
	ceiled_root = ceil(sqrt(num/2))
	if num == (ceiled_root * (2*ceiled_root-1)):
		return True
	else:
		return False
'''



#is_cyclic([8128, 2882, 8281])