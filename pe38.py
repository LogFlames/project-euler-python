def isPandigital(value):
    nums = []
    for n in str(value):
        nums += n

    nums.sort()
    if nums == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True
    return False

n = 1

biggestValue = 0

while len(str(n)) < 4.5:
    n += 1
    result = ""
    multValue = 0
    while len(result) < 9:
        multValue += 1
        result += str(n * multValue)
        if len(result) == 9 and isPandigital(result):
            if int(result) > biggestValue:
                biggestValue = int(result)

print(biggestValue)
