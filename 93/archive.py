# Given a string of nums and a string of operations,
# generate a string that represents an expression interleaving them.
def generate_strings(nums, ops):
    # Need to use izip_longest instead of zip,
    # because strings are of different length
    my_str = ''.join(i+j for i, j in izip_longest(nums, ops, fillvalue=''))
    return my_str
