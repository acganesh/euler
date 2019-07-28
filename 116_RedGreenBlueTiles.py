#Recursive solution:
#R(n) = R(n-1) + R(n-2) + 1
	#Case 1: first square is black.  Num ways: R(n-1)
	#Case 2: first square is filled.  Num ways: R(n-2)
	#Add another case for when the recursive part is completely empty.
#Similarly:
#G(n) = G(n) + G(n-3) + 1
#B(n) = B(n) + B(n-4) + 1
def main(n):
	vals_R = [0,1,2,4]
	vals_G = [0,0,1,2]
	vals_B = [0,0,0,1]
	length = 4
	while length < n:
		vals_R.append(vals_R[-1]+vals_R[-2]+1)
		vals_G.append(vals_G[-1]+vals_G[-3]+1)
		vals_B.append(vals_B[-1]+vals_B[-4]+1)

		length += 1
	return vals_R[-1]+vals_B[-1]+vals_G[-1]

print main(50)