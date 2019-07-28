from Euler import prime_sieve

#From proposition 2, https://sriasat.files.wordpress.com/2012/12/eureka.pdf
n = 20000000
r = 15000000
my_sum = 0

for p in prime_sieve(n):
	p_exp = p
	while p_exp <= n:
		my_sum += p * (n//p_exp - r//p_exp - (n-r)//p_exp)
		p_exp *= p
print my_sum
