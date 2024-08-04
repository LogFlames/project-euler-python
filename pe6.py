x = 0
y = 0
z = 0
a = 0
for i in range(1,101):
	x = i * i
	y = x + y
print y
for j in range(1,101):
	z = j + z
z = z * z
print z
a = z - y
print a