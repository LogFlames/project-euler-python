password = ""
testList = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729,
			710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

def pow(x, y):
    return x**y

# remove doublets in testList
cleanTest = []
for test in testList:
	if test not in cleanTest:
		cleanTest.append(test)

testList = cleanTest
# done

# determining the start number (the smallest possible based on the first number)
candidates = []
excluded = []
for test in testList:
	test = str(test)
	if test[0] not in candidates and test[0] not in excluded:
		candidates.append(test[0])
	if test[1] not in excluded:
		excluded.append(test[1])
	if test[2] not in excluded:
		excluded.append(test[2])

for test in range(len(candidates)-1,-1,-1):
	if candidates[test] in excluded:
		del candidates[test]

smallest = 10

for test in candidates:
	if int(test) < smallest:
		smallest = int(test)

if smallest == 10:
	smallest = 1

sum = smallest * pow(10, len(candidates) + len(excluded) - 1)
# done

while True:
	password = str(sum)
	savePas = password
	theSmallest = True
	counter = -1
	for a in list(password[::-1]):
		counter += 1
		if a == "4":
			sum += pow(10, counter) * 2
		if a == "5":
			sum += pow(10, counter)
			break
	if sum % 1000000 == 0:
		print(sum)

	for testPas in testList:
		testPas = str(testPas)
		password = savePas
		while True:
			if testPas[0] == password[0]:
				testPas = testPas[1:]
				password = password[1:]
			else:
				password = password[1:]
			if len(password) == 0 or len(testPas) == 0:
				break
		if len(testPas) != 0:
			theSmallest = False
			break
	if theSmallest:
		print(sum)
		break
	pasword = savePas
	sum += 1
