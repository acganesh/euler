def tri_num(n):
	return n*(n+1)/2

def square_num(n):
	return n*n

def pent_num(n):
	return n*(3*n-1)/2

def hex_num(n):
	return n*(2*n-1)

def hept_num(n):
	return n*(5*n-3)/2

def oct_num(n):
	return n*(3*n-2)

def get_nums(type, limit):
	ctr = 1
	nums = []
	num = 0
	while True:
		if type == 'tri':
			num = tri_num(ctr)
			t = 3
		elif type == 'square':
			num = square_num(ctr)
			t = 4
		elif type == 'pent':
			num = pent_num(ctr)
			t = 5
		elif type == 'hex':
			num = hex_num(ctr)
			t = 6
		elif type == 'hept':
			num = hept_num(ctr)
			t = 7
		elif type == 'oct':
			num = oct_num(ctr)
			t = 8

		if num > limit:
			break
		if num >= 1000:
			nums.append((t, num))
		ctr += 1
	return nums

#find number in list that starts with the string 'start'
def find_num(my_set, start):
	nums = []
	for num in my_set:
		if str(num[1])[:2] == start:
			nums.append(num)
	return nums

limit = 10000
tri_nums = get_nums('tri', limit)
square_nums = get_nums('square', limit)
pent_nums = get_nums('pent', limit)
hex_nums = get_nums('hex', limit)
hept_nums = get_nums('hept', limit)
oct_nums = get_nums('oct', limit)
empty = {'tri':set([]), 'square':set([]), 'pent':set([]), 'hex':set([]), 'hept':set([]), 'oct':set([])}


def find_all_nums(start):
	nums = []
	nums += find_num(tri_nums, start)
	nums += find_num(square_nums, start)
	nums += find_num(pent_nums, start)
	nums += find_num(hex_nums, start)
	nums += find_num(hept_nums, start)
	nums += find_num(oct_nums, start)
	return nums

all_starts = {}

for num in tri_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

for num in square_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

for num in pent_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

for num in hex_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

for num in hept_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

for num in oct_nums:
	start = str(num[1])[2:]
	starts = find_all_nums(start)
	if starts != []:
		all_starts[num] = tuple(starts)

print all_starts
ds = all_starts

def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print data, sum(data)
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types+[t], data+[n])

for type, data in all_starts: next([type], [data])

