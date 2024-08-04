import math

num = 2
sumDigit = 0
sumNum = 0

while True:
	num += 1
	if num % 100000 == 0: print num
	sumDigit = 0
	for numFactorial in str(num):
		sumDigit = sumDigit + math.factorial(int(numFactorial))
	if math.factorial(9)*len(str(num)) < num:
		break
	if sumDigit == num:
		sumNum = sumNum + num
print sumNum
