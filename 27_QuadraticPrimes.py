from math import sqrt, floor

def poly(list, x):
    my_sum = 0
    n = len(list)
    ctr = 0
    
    while ctr <= n-1:
        my_sum += (list[-ctr-1] * (x ** ctr))
        #print list[ctr-1], (x ** ctr), my_sum
        #print my_sum
        ctr += 1

    return my_sum

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    bound = sqrt(n)
    divisors = []

    i = 2
    while i <= bound:
            if (n % i) == 0:
                    return False
            i += 1
    return True

def test_primes(list):
    n = 0

    while isPrime(poly(list, n)):
        n += 1

    return n

#print test_primes([1, 1, 41])
#print test_primes([1, -79, 1601])
#print test_primes([1, -61, 971])


#2^2 + 2*2 + 3 = 11
max_primes = 0
max_product = 0
#from the polynomial n^2 - 79n + 1601

a = 1
b = 1

a_range = range(1,1001)
b_range = range(1,1001)
a_signs = [1, -1]
b_signs = [1, -1]

max_a = 0
max_b = 0


ctr = 0

for a_sign in a_signs:
    for b_sign in b_signs:
        for a in a_range:
            for b in b_range:
                a = a_sign*a
                b = b_sign*b

                num_primes = test_primes([1, a, b])
                #print num_primes
                if num_primes >= max_primes:
                    max_primes = num_primes
                    max_product = a*b
                    max_a = a
                    max_b = b
                #b += 1
                ctr += 1
            #a += 1
                #if ctr % 1000 == 0: print ctr

print max_product, max_primes, max_a, max_b
#Desired answer is max_product

