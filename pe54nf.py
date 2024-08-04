def getValueOfCard(x):
    if x == "T":
        return 10
    if x == "J":
        return 11
    if x == "Q":
        return 12
    if x == "K":
        return 13
    if x == "A":
        return 14
    return int(x)

royalFlush = ["T", "J", "Q", "K", "A"]
royalFlush.sort()

def RoyalFlush(hand):
    playerRoyalFlushTest = []
    for a in hand:
        playerRoyalFlushTest.append(a[0])
    if playerRoyalFlushTest == royalFlush:
        return True
    return False

def StraightFlush(hand):
    possibleStraightFlush = True
    currentValue = getValueOfCard(player1[0][0]) - 1
    kind = hand[1][0]
    for a in hand:
        if getValueOfCard(a[0]) == currentValue + 1 and a[1] == kind:
            currentValue = getValueOfCard(a[0])
        else:
            possibleStraightFlush = False
            break
    if possibleStraightFlush:
        return True
    return False

def FourOfAKind(hand):
    fourOfAKind = True
    kind = getValueOfCard(hand[0][0])
    canChange = True
    for a in hand:
        if getValueOfCard(a[0]) != kind and not canChange:
            fourOfAKind = False
        elif canChange:
            kind = getValueOfCard(a[0])
            canChange = False
    if fourOfAKind:
        return True
    return False

def getWinner(player1, player2):
    # royal flush
    if RoyalFlush(player1):
        return 1
    if RoyalFlush(player2):
        return 2

    # straight flush
    if StraightFlush(player1):
        return 1
    if StraightFlush(player2):
        return 2

    # four of a kind
    if FourOfAKind(player1):
        return 1
    if FourOfAKind(player2):
        return 2
