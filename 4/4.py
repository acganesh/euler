def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

# Use the fact that 6 digit palindromes have to be
# multiples of 11
def main():
    # All three digit multiples of 11
    mults = xrange(990, 99, -11)
    three_digit_nums = xrange(999, 99, -1)

    max_prod = 0
    for a in mults:
        for b in three_digit_nums:
            prod = a*b
            if is_palindrome(prod):
                max_prod = max(prod, max_prod)
    return max_prod

print main()

