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

def get_padded_val(L,x,y):
	try:
		return L[x][y]
	except:
		return float('Inf')

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
	return L

main_list = parse()
test_list = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

#ss_list = subset(main_list, 6)

print min_path_sum3(test_list)