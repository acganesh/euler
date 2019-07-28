'''
Seq: 4, 12, 20, 28, 
'''
'''
16, 32, 48
'''
'''
36, 60
''
Seq: 8, 16, 24, 32
'''

def generalized_seq(n, order, s_id, limit):
	def seq1(n):
		ctr = 1
		seq = [4]
		while ctr <= n:
			seq.append(seq[-1] + 8)
			ctr += 1
		return seq

	def seq2(n):
		ctr = 1
		seq = [8]
		while ctr <= n:
			seq.append(seq[-1] + 8)
			ctr += 1
		return seq

	if s_id == 1:
		if order == 1:
			return seq1(n)
		else:
			seq = [sum(seq1(order))]
	if s_id == 2:
		if order == 1:
			return seq2(n)
		else:
			seq = [sum(seq2(order))]
	ctr = 1
	while ctr <= n:
		seq.append(seq[-1] + 8*(order+1))
		ctr += 1
	return seq

def generalized_seq_L(order, s_id, limit):
	def seq1(limit):
		if 4 > limit:
			return []
		seq = [4]
		val = 1
		while True:
			val = seq[-1] + 8
			if val > limit:
				return seq
			seq.append(val)
		return seq

	def seq2(limit):
		if 8 > limit:
			return []
		seq = [8]
		val = 1
		while True:
			val = seq[-1] + 8
			if val > limit:
				return seq
			seq.append(val)
			ctr += 1
		return seq

	if s_id == 1:
		if order == 1:
			return seq1(limit)
		else:
			seq = [sum(seq1(order))]
	if s_id == 2:
		if order == 1:
			return seq2(limit)
		else:
			seq = [sum(seq2(order))]
	if seq == [0]:
		return []
	val = 1
	while True:
		val = seq[-1] + 8*(order+1)
		if val > limit:
			return seq
		seq.append(val)
		ctr += 1
	return seq

def main(limit):
	count = 0
	my_list = [1]
	order = 1
	for s_id in (1,2):
		while my_list != []:
			my_list = generalized_seq_L(order, s_id, limit)
			print my_list
			count += len(my_list)
			order += 1
		my_list = [1]
	return count

print main(32)
