import math

num = 0
sumDigit = 0

num = math.pow(2,1000)
num = int(num)
print num

for n in str(num):
	sumDigit += int(n)
print sumDigit
