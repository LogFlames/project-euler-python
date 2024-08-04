import math

num = 1
sumDigit = 0
sumNum = 0

while True:
	num += 1
	sumDigit = 0
	for numPow in str(num):
		sumDigit += math.pow(int(numPow), 5)
	if sumDigit == num:
		sumNum += num
		print sumNum
	if 9**5*len(str(num)) < num:
		break
print sumNum
