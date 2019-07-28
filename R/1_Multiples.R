#Finds the sum of the first N multiples of k
tri_sum <- function(N, k) {
	return(k*N*(N+1)/2)
}

main <- function(N, a, b) {
	limit_a = (N-1) %/% a
	limit_b = (N-1) %/% b
	limit_ab = (N-1) %/% (a*b)
	X = tri_sum(limit_a, a)
	Y = tri_sum(limit_b, b)
	Z = tri_sum(limit_ab, a*b)
	return(X+Y-Z)
}

main(1000, 3, 5)

#Elegant way to write the brute force method:
x < - seq(1,999)
sum(x[x %% 3 ==0 | x %% 5 == 0])