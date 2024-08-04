import math

stop = False

for c in xrange(1000):
	if stop:
		break
	for b in xrange(998):
		if stop:
			break
		a = 1000 - (c + b)
		if a < b < c:
			aPow = a**2
			bPow = b**2
			cPow = c**2
			if aPow + bPow == cPow and a + b + c == 1000:
				print a * b * c
				stop = True
				break
