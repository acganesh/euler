def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def sum_of_proper_divisors(n):
    pfs = prime_factors(n)
    pfs_set = set(pfs)

    prod = 1

    for item in pfs_set:
            exp = pfs.count(item)
            prod *= (item ** ((exp+1)) - 1)/(item - 1)
    prod -= n
    return prod

def sum_amicable_numbers(limit):
    num = 2
    amicable_sum = 0

    while num < limit:
        cur_sum = sum_of_proper_divisors(num)
        if num == sum_of_proper_divisors(cur_sum) and not num == cur_sum:
            print num, cur_sum
            amicable_sum += (num+cur_sum)

        num += 1

    print amicable_sum
    print "Halved sum:"
    print amicable_sum/2

sum_amicable_numbers(10000)