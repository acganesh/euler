from math import factorial

my_list = list(str(factorial(100)))

my_list_int = [int(x) for x in my_list]
my_sum = sum(my_list_int)

print my_sum
