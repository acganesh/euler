from math import sqrt

#A*(A-1)/S*(S-1) = 1/2
#2(A^2-A) = S^2-S

def main(n):
	vals = [0]*n
	for x in range(n):
		vals[x] = x**2 - x
	for val in vals:
		if 2*val in vals:
			print vals.index(val), vals.index(2*val)

#After experimenting:

#B vals follow the recursion
#a_n = 6*a_{n-1} - a_{n-2} - 2, with a_0 = 1, a_1 = 3
#a(n) = (((1+sqrt(2))^(2*n-1) - (1-sqrt(2))^(2*n-1))/sqrt(8)+1)/2.

def B(n):
	return (((1+sqrt(2))**(2*n-1) - (1-sqrt(2))**(2*n-1))/sqrt(8)+1)/2

#total follows the recursion
#a_n = 6*a_{n-1} - a_{n-2} - 2, with a_0 = 0, a_1 = 1
#closed form:1/2+1/4*sqrt(2)*((3+2*sqrt(2))^n-(3-2*sqrt(2))^n)-1/4*((3-2*sqrt(2))^n+(3+2*sqrt(2))^n)

def total(n):
	return 1./2+1./4*sqrt(2)*((3+2*sqrt(2))**n-(3-2*sqrt(2))**n)-1./4*((3-2*sqrt(2))**n+(3+2*sqrt(2))**n)

print total(17) > 10**12
print B(17)

