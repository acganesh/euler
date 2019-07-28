function gcd(a,b) {
	if (b) {
		return gcd(b, a % b);
	} else {
		return Math.abs(a);
	}
}

function lcm(a,b) {
	return (a*b) / gcd(a,b);
}

function main(N) {
	array = new Array(N);
	for (var i=0; i<N; i++) {
		array[i] = i+1;
	}
	return array.reduce(lcm);
}

console.log(main(20));
