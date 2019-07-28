from datetime import datetime

def first_n_digits():
	num = 23849037483904738940738490374893034348394839
	s1 = datetime.now()
	print num // (10 ** 40)
	print datetime.now() - s1
	#slow because representing 10**40 takes a long time

	s2 = datetime.now()
	print str(num)[:10]
	print datetime.now() - s2

	s3 = datetime.now()
	print str(num)[-10:]
	print datetime.now() - s3

	s4 = datetime.now()
	print num % (10 ** 10)
	print datetime.now() - s4




first_n_digits()
