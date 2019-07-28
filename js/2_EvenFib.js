function main(limit) {
	fib = [0, 1];
	len = 2; 
	sum = 0; 
	val = 1;
	
	while (val < limit) {
		val = fib[len-1] + fib[len-2];
		fib.push(fib[len-1]+fib[len-2]);
		if (val % 2 == 0) { sum += val; }
		len += 1;
	}
	return(sum);
}

console.log(main(4000000));