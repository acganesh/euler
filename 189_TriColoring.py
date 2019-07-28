def main():
	A = (3**4)*(2**20) #Reflection fixed point
	B = (3**2)*(2**15) #Rotation fixed point
	C = (2**36)*(3**4)#Identity fixed point

	A = (3**2)*(2**6)
	B = (3)*(2**5)
	C = (3**2)*(2**10)

	#(3*A+3*B)/6 from Burnside's Lemma
	return (3*A+2*B+C)/6

print main()