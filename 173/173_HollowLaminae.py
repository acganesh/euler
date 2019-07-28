from math import floor, sqrt


def factor(n):
    """Returns the factors of n by trial division.
    Note - it's probably more efficient to factor the first n numbers via a
    sieve."""
    limit = int(floor(sqrt(n)))
    factors = set()
    for i in range(2, limit+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n / i)
    return factors


def num_laminae(n):
    """To determine the number of laminae for a given number of tiles,
    we need to count solutions of the Diophatine equation k(2a + 8(k-1)) = 2n,
    where n is the number of tiles."""
    factors = factor(n)
    sols = []
    sol_count = 0
    for k in factors:
        a = (64/k - 8*(k-1))/2
        # If a is a positive integer, then (a, k)
        # corresponds to a valid lamina.
        if a > 0 and a == floor(a):
            sols.append((a, k))
            sol_count += 1
    return sol_count


def main(limit):
    """Counts the number of possible laminae with n tiles, not
    necessarily using all at once."""
    sol_count = 0
    for n in range(1, limit+1):
        sol_count += num_laminae(n)
    return sol_count

print main(1000000)
