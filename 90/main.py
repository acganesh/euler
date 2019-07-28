from itertools import permutations, combinations, product

def is_valid(d1, d2):
    def f(s):
        if s[0] in d1 and s[1] in d2:
            return True
        elif s[1] in d1 and s[0] in d2:
            return True
        return False


    def g(s):
        """Modified version of f."""
        result = f(s)
        if result: return result

        eq = ('6', '9')
        for v1, v2 in permutations(eq):
            if v1 in s:
                s2 = s.replace(v1, v2)
                result = f(s2)
                if result: return s2
        return False

    squares = []

    for x in range(1, 10):
        sq = str(x**2)
        if int(sq) < 10:
            sq = '0'+sq
        squares.append(sq)

    vals = map(g, squares)
    return all(vals)

def validate():
    d1 = ['0', '5', '6', '7', '8', '9']
    d2 = ['1', '2', '3', '4', '8', '9']
    assert is_valid(d1, d2) == True

    d1 = ['0', '5', '6', '7', '8', '9']
    d2 = ['1', '2', '3', '4', '6', '7']
    assert is_valid(d1, d2) == True
    print 'Tests passed!'

validate()

def main():
    digits = map(str, xrange(10))
    total = 0
    for d1, d2 in product(combinations(digits, 6), repeat=2):
        if is_valid(d1, d2):
            total += 1
    return total / 2

print main()

