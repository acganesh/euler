from Euler import perm
from math import factorial

n = 100
limit = 6000
length = 5
cubes = {}
min_cube = float('Inf')

while min_cube == float('Inf') or len(string) <= len(str(min_cube)):
	cube = n**3
	string = ''.join(sorted(str(cube)))
	if string in cubes:
		cubes[string] += [cube]
		if len(cubes[string]) == length:
			min_cube = min(min_cube, cubes[string][0])
	else:
		cubes[string] = [cube]
	n += 1

print min_cube