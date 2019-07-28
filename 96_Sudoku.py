S_test = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]]
S_test_3 = [[0,0,0,0,2,1,6,5,7],[9,6,7,3,4,5,8,2,1],[2,5,1,8,7,6,4,9,3],[5,4,8,1,3,2,9,7,6],[7,2,9,5,6,4,1,3,8],[1,3,6,7,9,8,2,4,5],[3,7,2,6,8,9,5,1,4],[8,1,4,2,5,3,7,6,9],[6,9,5,4,1,7,3,8,2]]

S_test2 = tuple(tuple(x) for x in S_test)

def parse():
	line_ctr = 0
	board_ctr = 0
	data = []
	board = []
	row = []
	with open('96_data.txt', 'rb') as f:
		for line in f:
			if not 'Grid' in line:
				row = [int(num) for num in line if num != '\n']
				board.append(row)
			if len(board) == 9:
				data.append(board)
				board = []
	return data

parse()


#generates a list of candidates for the board S at coordinates x, y
def candidates(S, x, y):
	val = S[x][y]
	if val != 0:
		return []
	else:
		S_T = zip(*S)
		cands = set(range(0, 10))
		def row_candidates():
			row = S[x]
			#print 'row', row
			for num in row:
				if num in cands:
					cands.remove(num)

		def col_candidates():
			col = S_T[y]
			#print 'col', col
			for num in col:
				if num in cands:
					cands.remove(num)

		def subgrid_ind():
			return x/3,y/3

		def get_subgrid(x,y):
			vals = []
			x_s = 3*(x/3)
			y_s = 3*(y/3)
			for x in range(x_s, x_s + 3):
				for y in range(y_s, y_s + 3):
					val = S[x][y]
					vals.append(val)
			return vals

		def subgrid_candidates(x,y):
			vals = []
			x_s = 3*(x/3)
			y_s = 3*(y/3)
			for x in range(x_s, x_s + 3):
				for y in range(y_s, y_s + 3):
					val = S[x][y]
					if val in cands:
						cands.remove(val)

		row_candidates()
		col_candidates()
		subgrid_candidates(x,y)
		#print 'sub',get_subgrid(x,y)
		return cands

def get_cand_grid(S):
	C = [[0]*9 for _ in range(9)]
	for x in range(9):
		for y in range(9):
			C[x][y] = candidates(S, x, y)
	return C

def get_cand_list(S):
	cand_grid = get_cand_grid(S)
	D = []
	for x in range(9):
		for y in range(9):
			for z in cand_grid[x][y]:
				S_temp = list(list(x) for x in S)
				S_temp[x][y] = z
				D.append(S_temp)
	return D

def is_complete(board):
	for x in range(9):
		for y in range(9):
			if board[x][y] == 0:
				return False
	return True

D = {}
def next(cands, board):
	if is_complete(board):
		print board
	else:
		board_key = tuple(tuple(x) for x in board)
		cands = D.get(board_key, get_cand_list())
		if board_key in D.keys():
			cands = D[board_key]
		else:
			cands = get_cand_list(board)
			D[board_key] = cands
		for c in cands:
			next(cands, c)
			#print D

def is_valid(C):
	for row in C:
		for c in row:
			if c != set([]):
				return True
	return False

def solve(S):
	i = 0
	j = 0

	if is_complete(S):
		#print("Board solved!")
		print S
		return
	else:
		for x in range(9):
			for y in range(9):
				if S[x][y] == 0:
					i = x
					j = y
			else:
				continue
			break
	c_list = candidates(S, i, j)

	for c in c_list:
		S[i][j] = c
		solve(S)

	S[i][j] = 0

def main():
	main.total = 0
	def solve(S):
		i = 0
		j = 0

		if is_complete(S):
			#print("Board solved!")
			main.total += int(''.join([str(x) for x in S[0][:3]]))
			return
		else:
			for x in range(9):
				for y in range(9):
					if S[x][y] == 0:
						i = x
						j = y
				else:
					continue
				break
		c_list = candidates(S, i, j)

		for c in c_list:
			S[i][j] = c
			solve(S)

		S[i][j] = 0
	data = parse()
	for board in data: solve(board)
	print main.total
					



#print candidates(S_test, 0, 0)

def tests():
	#print get_cand_grid(S_test)
	#print get_cand_list(S_test)
	a= solve(S_test)
	print a

main()


