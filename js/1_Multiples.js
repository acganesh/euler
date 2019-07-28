// If m and n are relatively prime, return the sum of multiples of m and n below K.
function main(m, n, K) {
	val1 = m*tri_sum(Math.floor((K-1)/m));
	val2 = n*tri_sum(Math.floor((K-1)/n));
	val3 = m*n*tri_sum(Math.floor((K-1)/(m*n)));
	return (val1 + val2 - val3);
}

//Returns the sum of the first n integers.
function tri_sum(n) {
	return n*(n+1)/2;
}

console.log(main(3, 5, 1000));