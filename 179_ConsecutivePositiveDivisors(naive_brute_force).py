from math import sqrt


#Super inefficient
def num_divisors(n):
  bound = sqrt(n)
  divisors = []

  i = 1
  while i <= bound:
    if (n % i) == 0:
      divisors.append(i)
      divisor_pair = n/i
      if not (i == n/i):
        divisors.append(n/i)
    i += 1
  return len(divisors)


import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
'''
def num_divisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)
'''


limit = 10 ** 7
num = 1
total = 0
start = True

while num < limit:
  if start:
    num1 = num_divisors(num)
    num2 = num_divisors(num + 1)
    num += 1

  else:
    num1 = num2
    num2 = num_divisors(num + 1)
    num += 1

  if num1 == num2:
    total += 1

  if num % 1000000 == 0: print num

print total
