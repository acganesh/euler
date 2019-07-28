from math import sqrt

def isPrime(n):
        bound = sqrt(n)
        divisors = []

        i = 2
        while i <= bound:
                if (n % i) == 0:
                        return False
                i += 1
        return True

def getPrimes(limit):
        primes = []
        i = 2
        while (len(primes) < limit):
                if isPrime(i):
                        primes.append(i)
                i += 1
        return primes

prime_list = getPrimes(80000)
my_sum = 0
max_length = 0
max_sum = 0
max_chain_ends = None

start_indices = range(0, 1000)


for start in start_indices:
        my_sum = 0
        ctr = 0
        while my_sum < 1000000:
                my_sum += prime_list[start+ctr]
                ctr += 1

                if ctr > max_length and isPrime(my_sum):
                        max_length = ctr
                        max_chain_ends = [prime_list[start], prime_list[start+ctr]]
                        max_sum = my_sum

print max_length
print max_chain_ends
print max_sum