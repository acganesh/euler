from itertools import permutations, combinations_with_replacement, count, combinations

def parse_rpn(expression):
    """Evaluate a postfix/RPN expression.
    Source:
    http://danishmujeeb.com/blog/2014/12/parsing-reverse-polish-notation-in-python"""
    stack = []

    for val in expression.split(' '):
      if val in ['-', '+', '*', '/']:
          op1 = stack.pop()
          op2 = stack.pop()
          if val=='-': result = op2 - op1
          if val=='+': result = op2 + op1
          if val=='*': result = op2 * op1
          if val=='/': result = op2 / op1
          stack.append(result)
      else:
          stack.append(float(val))

    return stack.pop()


# Calculate all possible postfix expressions for
# a given set of digits and operations
def compute(nums, ops):
    my_string = nums+ops
    vals = set([])
    gen = (s for s in permutations(my_string))
    for s in gen:
        combined = ' '.join(s)
        try:
            val = parse_rpn(combined)
            if val > 0 and int(val) == val:
                vals.add(val)
        # Catch cases where postfix expression is invalid
        except (IndexError, ZeroDivisionError):
            pass
    return vals

# Calculate all possible values for a given set of digits
def get_all_vals(nums):
    nums = ''.join(nums)
    all_ops = '+-*/'
    vals = set([])

    for ops in combinations_with_replacement(all_ops, 3):
        ops = ''.join(ops)
        vals = vals.union(compute(nums, ops))

    return vals


# Return n the highest value such that {1,2,...,n} is in vals
def get_max_chain(vals):
    for i in count(1):
        if i not in vals: return i-1

# Run tests
def validate():
    vals = get_all_vals('1234')
    max_n = get_max_chain(vals)
    assert len(vals) == 31
    assert max(vals) == 32
    assert max_n == 28


# Iterate through all possible sets of digits {a, b, c, d},
# computing the maximum value of n
def main():
    all_nums = '123456789'
    max_n = 0
    max_nums = None
    for nums in combinations(all_nums, 4):
        vals = get_all_vals(nums)
        n = get_max_chain(vals)
        if n > max_n:
            max_n = n
            max_nums = nums
    return max_nums

# validate()
print main()
