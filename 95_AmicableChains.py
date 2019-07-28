# Factorize the first million integers using a sieve
def factor_sieve(n):
    sieve = [[] for x in range(n+1)]
    for x in range(2, n+1):
        if sieve[x] == []:
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                sieve[y].append((x, exp-1))
    return sieve

# Here, we let sigma denote the sum of an integer's proper divisors (not the
# sum of divisors, as is conventional).
def sigma(n):
    fact = sieve[n]
    val = 1
    for prime, exp in fact:
        val *= ((prime**(exp+1)-1)/(prime-1))
    return val - n

limit = 10**6
sieve = factor_sieve(limit)


def main(limit):
    # Map n to integers corresponding to the length of the chain,
    # or "False" if the chain doesn't satisfy the desired condition.
    data = {}
    max_length = 0
    max_chain = []

    for i in range(1, limit):
        chain = [i]
        vals = set(chain)

        while True:
            val = sigma(chain[-1])
            # Success condition
            if val == i:
                length = len(chain)
                data[i] = length
                if length > max_length:
                    max_length = length
                    max_chain = chain
                break
            # Failure conditions
            elif val in vals or val > limit:
                data[i] = False
                break
            # Continue adding to chain
            else:
                vals.add(val)
                chain.append(val)
                length = len(chain)
    return min(max_chain)


print main(limit)
