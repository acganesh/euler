# -*- coding: utf-8 -*-

from Euler import prime_sieve

solved = range(1,60)+range(62,68)+range(69,75)+range(78,82)+range(99,103)+range(114,118)+range(124,128)
stray = [76, 85, 87, 89, 92, 97, 108, 112, 120, 121,145,179,183,187,188,190,191,203,205,206,231,235,301,407,500,504]

solved = solved + stray
solved_set = set(solved)

def num_solved():
	print "You've solved", len(solved)

def as_easy_as_pi():
	list = [3,14,15,92,65,35,89,79,32,38,46]
	unsolved = set([])
	for num in list:
		if num not in solved_set:
			unsolved.add(num)
	print "As Easy As Pi, solve:", unsolved

def unlucky_squares():
	squares = set([x**2 for x in range(1,24)])
	square_count = 0
	for num in solved_set:
		if num in squares:
			square_count += 1
	print "Unlucky Squares, solve:", 13 - square_count

def prime_obsession():
	primes = set(prime_sieve(510))
	prime_count = 0
	for num in solved_set:
		if num in primes:
			prime_count += 1
	print "Prime Obsession, solve:", 50 - prime_count

def ternary_triumph():
	list = [1,3,9,27,81,243]
	unsolved = set([])
	for num in list:
		if num not in solved_set:
			unsolved.add(num)
	print "Ternary Triumph", unsolved

def fibonacci_fever():
	def fib(n):
		vals = [1,1]
		length = 2
		while length < n:
			vals.append(vals[-1]+vals[-2])
			length += 1
		return vals
	list = fib(12)
	unsolved = set([])
	for num in list:
		if num not in solved_set:
			unsolved.add(num)
	print "Fibonacci Fever", unsolved

def triangle_trophy():
	def tri(n):
		vals = [1]
		length = 1
		while length < n:
			vals.append((length+1)*(length+2)/2)
			length += 1
		return vals
	list = tri(25)
	unsolved = set([])
	for num in list:
		if num not in solved_set:
			unsolved.add(num)
	print "Triangle Trophy", unsolved

def lucky_luke():
	def get_lucky(n):
	    lucky = list(range(1, n+1, 2))
	    current_index = 1
	    current = 3
	    while current < len(lucky):
	        lucky = [a for i,a in enumerate(lucky) if (i+1)%current]
	        current_index += 1
	        current = lucky[current_index]
	    return lucky
	lucky = get_lucky(510)
	lucky_count = 0
	for num in solved_set:
		if num in lucky:
			lucky_count += 1
	print "Lucky Luke, solve:", 50 - lucky_count

def one_percenter():
	print "One Percenter: You just need to solve " + str(124-len(solved)) + " more!"






def main():
	num_solved()
	as_easy_as_pi()
	unlucky_squares()
	prime_obsession()
	ternary_triumph()
	fibonacci_fever()
	triangle_trophy()
	lucky_luke()
	one_percenter()

main()
