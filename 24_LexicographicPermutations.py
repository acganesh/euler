from itertools import permutations

def get_perms(num):
	my_str = sorted(str(num))
	perms = [''.join(p) for p in permutations(my_str)]
	return perms

perms = get_perms(9876543210)
print perms[999999]
