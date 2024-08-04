# 'fib1' = the last fibonacci number, 'fib2' and 'fib3' = the used fibonacci number, 'evenFib' is all of the even fibonacci added together.
fib1 = 1
fib2 = 0
fib3 = 1
evenFib = []
while True:
	fib3 = fib1 + fib2
	fib1 = fib2
	fib2 = fib3
	if (fib3 > 4e6):
		break
	if (fib3 % 2 == 0):
		evenFib.append(fib3)
print sum(evenFib)
