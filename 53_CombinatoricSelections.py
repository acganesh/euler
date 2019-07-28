from math import factorial, ceil

def n_choose_k(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

limit = 100
start = 10

n = start

count = 0

while n <= 100:
    current_count = 0
    mid_point = ceil(n/2)
    k = mid_point   

    while n_choose_k(n, k) > 1000000:
        k += 1
        current_count += 1


    if n%2 == 0:
        if current_count > 0:
            count += current_count*2 -1
        #print n, count
    elif n%2 == 1:
        if current_count > 0:
            count += (current_count-1)*2
        #print n, count
    n += 1

print count