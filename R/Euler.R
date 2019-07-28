fib <- function(N) {
	vals <- c(0, 1)
	ctr <- 1
	for (i in 1:N) {
		val = sum(tail(vals, n=2))
		vals <- append(vals, val)
	}
	return(vals)
}