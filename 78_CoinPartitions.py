mod = 10**6

def pentagonal(n):
    return n*(3*n-1)/2

def gen_pent(n):
    n = n-1
    my_list = [0]
    num = 1
    ctr = 1
    while True:
        my_list.append(num)
        ctr += 1
        if ctr > n:
            break
        my_list.append((-1)*num)
        ctr +=1 
        num +=1 
        if ctr > n:
            break
    return my_list

def main(N):
    mod = 10 **6
    pents = [pentagonal(x) for x in gen_pent(N)]
    partitions = [0] * N
    partitions[0] = 1

    num = 1
    while num < N:
        ctr = 1
        while num - pents[ctr] >= 0:
            pent = pents[ctr]
            partitions[num] += ((-1)**((ctr-1)/2)*partitions[num - pent]) % mod
            ctr += 1
        if partitions[num] % 1000000 == 0:
            print num
        num += 1

main(100000)
