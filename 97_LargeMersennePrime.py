exponent = 7830457
factor = 28433

num = 100
a = 2 ** num

mod = 10 ** 11


modded_a = a % mod 
modded_exp = exponent % num

result = 1

while num <= exponent:
    result = (result % mod) * modded_a
    num += 100

result = (result % mod) * ((2 ** modded_exp) % mod)

print (result*factor + 1) % mod 

