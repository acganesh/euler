import datetime

start = datetime.datetime.now()

#@profile
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

#@profile
def sigma(n):
    pfs = prime_factors(n)
    pfs_set = set(pfs)

    prod = 1

    for item in pfs_set:
            exp = pfs.count(item)
            prod *= (item ** ((exp+1)) - 1)/(item - 1)
    return prod

#@profile
def per_def_abu(n):
    val = sigma(n) - n
    if val < n:
    	return 'deficient'
    elif val > n:
    	return 'abundant'
    elif val == n:
    	return 'perfect'

def is_abundant_sum(n, abundant_nums):
    for abundant_num in abundant_nums:
        if abundant_num > n: #Adding this sped it up for n = 5000 from 28s to 12s!
            return False
        if n - abundant_num in abundant_nums:
            return True
    return False

#@profile
def main(limit):
    #limit = 100
    my_list = range(limit+1)

    abundant_nums = []

    n = 1
    while n < limit:
    	if per_def_abu(n) == 'abundant':
    		abundant_nums.append(n)
    	n += 1

    #pairwise_sums = []
    subtract_this = 0
    ctr = 0
    indices = []
    #print len(abundant_nums)
    #print abundant_nums

    abundant_nums = set(abundant_nums) #Adding this sped it up from 12s to 0.04s for n = 5000!
    my_sum = 0

    num = 1

    non_abundant = []

    while num <= limit:
        if not(is_abundant_sum(num, abundant_nums)):
            non_abundant.append(num)
            my_sum += num
        num += 1
        #print num

    print my_sum

main(28123)
print datetime.datetime.now() - start

#Searching in lists takes a long time. Set datastructure makes this so much faster.  Using binary search is also far far more efficient.


#By mathematical analysis, it can be shown that all 
#integers greater than 28123 can be written as the sum of two abundant numbers. 


