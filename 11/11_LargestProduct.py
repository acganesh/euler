data = []
with open('11_data.txt', 'rb') as f:
	for line in f:
		 data.append([int(x) for x in line.split()])

print data

def horizontal_products(data):
	max_prod = 0
	for i in range(17):
		for j in range(20):
			prod = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j]
			if prod > max_prod: max_prod = prod
	return max_prod

def vertical_products(data):
	max_prod = 0
	for i in range(20):
		for j in range(17):
			prod = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3]
			if prod > max_prod: max_prod = prod
	return max_prod

def SW_diagonal_products(data):
	max_prod = 0
	for i in range(17):
		for j in range(17):
			prod = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3]
			if prod > max_prod: max_prod = prod
	return max_prod

def SE_diagonal_products(data):
	max_prod = 0
	for i in range(3, 20):
		for j in range(17):
			prod = data[i][j] * data[i-1][j+1] * data[i-2][j+2] * data[i-3][j+3]
			if prod > max_prod: max_prod = prod
	return max_prod

print max(horizontal_products(data), vertical_products(data), SW_diagonal_products(data), SE_diagonal_products(data))
