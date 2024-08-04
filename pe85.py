def getAllSquares(x, y):
    num = 0
    for x_ in range(1, x + 1):
        for y_ in range(1, y + 1):
            num += scl(x, x_) * scl(y, y_)

    return num

def scl(valMax, val):
    tempList = []
    for n in range(valMax):
        tempList.append(n + 1)

    return tempList[len(tempList) - val]

def getClosest(numA, numB, numC):
    aDif = abs(numC - numA)
    bDif = abs(numC - numB)
    if aDif < bDif:
        return numA
    else:
        return numB

def testBreak(closest_, lastClosest_, thisDim_):
    if abs(closest_ - lastClosest_) < abs(closest_ - thisDim_):
        return True
    else:
        return False

def findBounds(solution):
    closest = 0
    lastClosest = closest
    x = 0
    y = 1
    thisDim = 10
    while True:
        x += 1
        thisDim = getAllSquares(x, y)
        lastClosest = closest
        closest = getClosest(thisDim, closest, solution)
        if testBreak(closest, lastClosest, thisDim):
            print(closest)
            return [x * 1.5, y * 1.5]
        y += 1
        thisDim = getAllSquares(x, y)
        lastClosest = closest
        closest = getClosest(thisDim, closest, solution)
        if testBreak(closest, lastClosest, thisDim):
            print(closest)
            return [x * 1.5, y * 1.5]

def findNearestSolution(bounds, solution):
    closest = [0, 0, 0]
    lastClosest = closest
    thisDim = 0
    bounds[0] = int(bounds[0])
    bounds[1] = int(bounds[1])
    for x in range(1, bounds[0] + 1):
        for y in range(1, bounds[1] + 1):
            thisDim = getAllSquares(x, y)
            lastClosest = closest[0]
            closest[0] = getClosest(thisDim, closest[0], solution)
            if closest[0] != lastClosest:
                closest[1] = x
                closest[2] = y

    return closest

bounds = findBounds(2000000)
nearestSol = findNearestSolution(bounds, 2000000)
print(nearestSol)
print(nearestSol[1] * nearestSol[2])
