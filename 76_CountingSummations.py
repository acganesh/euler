#http://www.programminglogic.com/integer-partition-algorithm/
#A1

cache = [[0]*(101) for _ in range(101)]

def partition1(N, max_num):

    if max_num == 0:
        return 0
    if N == 0:
        return 1
    if (N < 0):
        return 0

    if cache[N][max_num] != 0:
        return cache[N][max_num]
    cache[N][max_num] = partition1(N, max_num-1) + partition1(N - max_num, max_num)

    return cache[N][max_num]

print partition1(100, 99)