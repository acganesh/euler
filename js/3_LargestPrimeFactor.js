//Returns an array of booleans returning the primality of the indices
function sieve(limit) {
	//Initialization
	var s = new Array(limit);
	for (var i = 0; i < s.length; i++) {
		s[i] = true;
	}
	s[0] = false;
	s[1] = false;

	//Sieve iteration
	for (var i = 0; i < limit; i++) {
		if (s[i] == true) {
			for (var j = 2; i*j < limit; j++) {
				s[i*j] = false;
			}
		}
	}
	return s
}

//Returns the largest prime factor of N
function main(N) {
	sq_limit = Math.floor(Math.sqrt(N));
	s = sieve(sq_limit);
	for (i = 1; i <= sq_limit; i ++) {
		val = sq_limit - i;
		if (s[val] == true) {
			if (N % val == 0) { return val; }
		}
	}
}

console.log(main(600851475143));

