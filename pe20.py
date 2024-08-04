import math

sumDigit = 0
num = 100
numFactorial = math.factorial(num)
strNum = str(numFactorial)

for numFactorial in strNum:
	sumDigit = sumDigit + int(numFactorial)
print sumDigit
