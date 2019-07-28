#Project Euler Problem 62

digits, min_cube, n, d = '', float('Inf'), 100, 5
cubes = {}

while min_cube == float('Inf') or len(digits) <= len(str(min_cube)):
    c = n*n*n
    digits = ''.join(sorted(str(c)))
    if digits in cubes:
        cubes[digits] += [c]
        if len(cubes[digits]) == d:
            min_cube = min(min_cube, cubes[digits][0])
    else:
        cubes[digits] = [c]
    n += 1    
print min_cube