from Euler import prime_sieve, is_prime
from itertools import permutations as perms


def is_valid(my_list):
    return all((is_prime(str(p[0])+str(p[1]))) for p in perms(my_list, 2))


def iter_loop(my_list, primes, N):
    if len(my_list) == N:
        return my_list
    for p in primes:
        if p > my_list[-1] and is_valid(my_list + [p]):
            result = iter_loop(my_list + [p], primes, N)
            if result:
                return result
    return False


def main(N=5):
    primes = prime_sieve(10000)
    result = False
    while not result:
        my_list = [primes.pop(0)]
        result = iter_loop(my_list, primes, N)

    return sum(result)


if __name__ == '__main__':
    print main()
