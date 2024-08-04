def removeDublets(list_):
    index = 0
    while index < len(list_):
        for n in range(len(list_) - 1, index, -1):
            if list_[n] == list_[index]:
                del list_[n]
        index += 1
    return list_

def copyList(listToCopy):
    newList = []
    for n in listToCopy:
        newList.append(n)

    return newList

def waysToCreate(num, waysToCreateN, targetNum):
    if num == 1:
        return waysToCreate(num + 1, [], targetNum)
    elif num == 2:
        return waysToCreate(num + 1, [[1, 1]], targetNum)

    saveWaysToCreateN = copyList(waysToCreateN)

    print(str(num) + " / " + str(targetNum))

    for n in range(len(waysToCreateN)):
        for nn in range(len(waysToCreateN[n])):
            waysToCreateN.append(copyList(waysToCreateN[n]))
            waysToCreateN[len(waysToCreateN) - 1][nn] += 1

    for n in range(len(saveWaysToCreateN)):
        saveWaysToCreateN[n].append(1)
        waysToCreateN.append(saveWaysToCreateN[n])

    for n in range(len(waysToCreateN)):
        waysToCreateN.sort()

    waysToCreateN = removeDublets(waysToCreateN)

    if num == targetNum:
        return len(waysToCreateN)
    else:
        return waysToCreate(num + 1, waysToCreateN, targetNum)

print(waysToCreate(0, [], 100))
