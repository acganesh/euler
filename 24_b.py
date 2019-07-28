import itertools
def permute(n):
    permList = itertools.permutations(str(n))
    sorted(permList)
    print permList[len(permList - 1)]

def test(n):
    result = itertools.permutations(str(n))
    return result

result = test(123)
my_list = list(result)
print my_list

