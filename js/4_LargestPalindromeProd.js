//Use optimization that one of the three digit factors must be a multiple of 11.
function get_cands() {
	candidates = [];
	val = 110;
	for (var i = 11; 100 <= val && val < 1000; i++) {
		candidates.push(val);
		val = 11*i;
	}
	return candidates;
}

function is_palindrome(N) {
	s = String(N);
	return (s == s.split('').reverse().join(''));
}

function main() {
	max = 0
	candidates = get_cands();
	len = candidates.length;
	for (var j = 999; j >= 100; j--) {
		for (var i = 0; i < len; i++) {
			cand = candidates[len-i-1];
			val = j*cand;
			if (is_palindrome(val) == true && val > max) {
				max = val;
			}
		}
	}
	return max
}

console.log(main());