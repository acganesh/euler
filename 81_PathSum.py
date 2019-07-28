import csv
import itertools
import datetime

start = datetime.datetime.now()

def parse():
	my_list= []
	line = 'init'

	with open('81_data.txt', 'rb') as f:
		reader = csv.reader(f)
		for item in reader:
			item_int = [int(x) for x in item]
			my_list.append(item_int)
	return my_list

#brute force
def min_path_sum(my_list):
	strings = itertools.permutations('RD'*(len(my_list)-1))
	min_sum = float('Inf')
	min_str = None
	init = my_list[0][0]
	for string in strings:
		broken = False
		x = 0
		y = 0
		total = init
		for char in string:
			if char == 'D':
				x += 1
			elif char == 'R':
				y += 1
			total += my_list[x][y]
			if total > min_sum:
				broken = True
				break
		if total < min_sum and not broken:
			min_sum = total
			min_str = string
	return min_sum, min_str

#from bottom to top -- efficient algo
#wrong though, because it's greedy
def min_path_sum2(my_list):
	length = len(my_list)
	x = -1
	y = -1
	start = my_list[x][y]

	total = start
	string = ''

	while x >= -length+1 and y >= -length+1:
		val1 = my_list[x-1][y]
		val2 = my_list[x][y-1]
		if val1 < val2:
			x -= 1
			total += val1
			string += 'D'
		else:
			y -= 1
			total += val2
			string += 'R'
	total += my_list[0][0]

	return total, ''.join(string[::-1])


def get_padded_val(L,x,y):
	if x < 0 or y < 0:
		return float('Inf')
	else:
		return L[x][y]
#from top to bottom, but dynamically
def min_path_sum3(my_list):
	length = len(my_list)
	L = [[float('Inf')]*length for i in range(length)]
	L[0][0] = my_list[0][0]
	x = 1
	y = 0
	my_sum = 1
	while my_sum <= 2*(length-1):
		if length - my_sum > 0:
			x = my_sum
			y = 0
		else:
			x = length-1
			y = my_sum - x
		x_limit = y
		while x >= x_limit:
			if L[x][y] == float('Inf'):
				L[x][y] = min(get_padded_val(L, x-1, y), get_padded_val(L, x, y-1)) + my_list[x][y]
			x -= 1
			y += 1
		my_sum += 1
	return L[length-1][length-1]

def subset(my_list, n):
	ss_list = []
	my_list = my_list[:n]
	for item in my_list:
		ss_list.append(item[:n])
	return ss_list

test_list = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
main_list = parse()
#ss_list = subset(main_list, 6)

print min_path_sum3(main_list)

print datetime.datetime.now() - start




