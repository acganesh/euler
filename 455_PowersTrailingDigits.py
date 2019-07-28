'''
def f(n):
	lim = 10 ** 6
	s = 0
	my_max = 0

	for x in xrange(2, lim):
		if pow(n, x, 10 ** 9) == x and x > my_max:
			my_max = x
	return my_max

limit = 10 ** 3
n = 2
my_sum = 0

while n <= limit:
	my_sum += f(n)
	n += 1
'''

'''
Let f(n) be the largest positive integer x less than 10**9 
such that the last 9 digits of nx form the number x 
(including leading zeros), or zero if no such integer exists.

For example:

f(4) = 411728896 (4411728896 = ...490411728896)
f(10) = 0
f(157) = 743757 (157743757 = ...567000743757)
Σf(n), 2 ≤ n ≤ 103 = 442530011399
Find Σf(n), 2 ≤ n ≤ 106.

n^x == x (mod 10 ** 9)
'''

L, s = 1000000, 0

for n in xrange(2, L):
    x0, x1 = 0, n
    while x0 != x1 and x1:
        x0, x1 = x1, pow(n, x0, 10**9)
        print x0, x1
        import time; time.sleep(5)
    print x1
    print x0
    time.sleep(5)
    s += x1

print "Project Euler 455 Solution =", s

#x0,x1
#0, n
#n, 1
#1, n^n
#n^n n^n^n
#

