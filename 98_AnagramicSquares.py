import itertools

def main(n):
	squares = set([x**2 for x in range(1000)])
	square_perms = {}
	for item in squares:
		item = str(item)
		perms = list(map("".join, itertools.permutations(item)))[1:]
		for perm in perms:
			if int(perm) in squares:
				if item > int(perm) and item != perm and perm[0] != '0':
					if item in square_perms.keys():
						if item not in square_perms[item]:
							square_perms[item].add(perm)
					else:
						square_perms[item] = set([perm])


main(1000)