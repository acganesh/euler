main <- function(N) {
	vals <- c(0, 1)
	val <- 1
	sum <- 0
	while (val < N) {
		val = sum(tail(vals, n=2))
		vals <- append(vals, val)
		if (val %% 2 == 0) {
			sum <- sum + val
		}
	}
	return(sum)
}

main(4E6)