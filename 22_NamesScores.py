import csv


with open('22_data.txt', 'rb') as f:
	my_csv = csv.reader(f)
	for line in my_csv:
		data = line

data.sort()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

total_score = 0
ctr = 1

for item in data:
	cur_score = 0
	#print item
	for char in list(item):
		#print char
		alpha_index = alphabet.index(char) + 1
		cur_score += alpha_index
	cur_score *= ctr
	if item == "COLIN":
		print item
		print cur_score
		print ctr
	total_score += cur_score
	ctr += 1

print total_score



