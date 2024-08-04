count = 0
i = 0

for i in xrange(1, 1001):
	if i == 1000:
		count += 11
		i = i - 1000
	if i >= 900:
		count += 11
		if i > 900:
			count += 3
		i = i - 900
	if i >= 800:
		count += 12
		if i > 800:
			count += 3
		i = i - 800
	if i >= 700:
		count += 12
		if i > 700:
			count += 3
		i = i - 700
	if i >= 600:
		count += 10
		if i > 600:
			count += 3
		i = i - 600
	if i >= 500:
		count += 11
		if i > 500:
			count += 3
		i = i - 500
	if i >= 400:
		count += 11
		if i > 400:
			count += 3
		i = i - 400
	if i >= 300:
		count += 12
		if i > 300:
			count += 3
		i = i - 300
	if i >= 200:
		count += 10
		if i > 200:
			count += 3
		i = i - 200
	if i >= 100:
		count += 10
		if i > 100:
			count += 3
		i = i - 100
	if i >= 90:
		count += 6
		i = i - 90
	if i >= 80:
		count += 6
		i = i - 80
	if i >= 70:
		count += 7
		i = i - 70
	if i >= 60:
		count += 5
		i = i - 60
	if i >= 50:
		count += 5
		i = i - 50
	if i >= 40:
		count += 5
		i = i - 40
	if i >= 30:
		count += 6
		i = i - 30
	if i >= 20:
		count += 6
		i = i - 20
	if i == 19:
		count += 8
		i = i - 19
	if i == 18:
		count += 8
		i = i - 18
	if i == 17:
		count += 9
		i = i - 17
	if i == 16:
		count += 7
		i = i - 16
	if i == 15:
		count += 7
		i = i - 15
	if i == 14:
		count += 8
		i = i - 14
	if i == 13:
		count += 8
		i = i - 13
	if i == 12:
		count += 6
		i = i - 12
	if i == 11:
		count += 6
		i = i - 11
	if i == 10:
		count += 3
		i = i - 10
	if i == 9:
		count += 4
		i = i - 9
	if i == 8:
		count += 5
		i = i - 8
	if i == 7:
		count += 5
		i = i - 7
	if i == 6:
		count += 3
		i = i - 6
	if i == 5:
		count += 4
		i = i - 5
	if i == 4:
		count += 4
		i = i - 4
	if i == 3:
		count += 5
		i = i - 3
	if i == 2:
		count += 3
		i = i - 2
	if i == 1:
		count += 3
		i = i - 1
print count
