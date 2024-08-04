# This is the solution to ProjectEuler 96.

# https://projecteuler.net/problem=96

from os import path

# Test if the computer running it have multiprocessing downloaded
try:
    from multiprocessing import Pool
    useMultithreading = True
except:
    useMultithreading = False

sudokus = []

__codeDir = path.dirname(__file__)

# Copy a list so the new list doesn't point to the same points in memory
def copyList(listToCopy):
    newList = []
    for a in listToCopy:
        toAddToNewList = []
        for b in a:
            toAddToNewList.append(b)
        newList.append(toAddToNewList)

    return newList

# calculate all integers that can go in every square on the sudoku
# Ex: In this square the numbers: 1, 4 and 5 can be placed.
def calculatePossibleIntegers(sudoku):
    Change = True
    while Change:
        Change = False

        # create the strukture with lists that we will save what numbers can be used in
        #
        #[[], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], [],
        # [], [], [], [], [], [], [], [], []]
        posInt = []
        for a in range(9):
            toAddA = []
            for b in range(9):
                toAddA.append([])
            posInt.append(toAddA)

        # go thru all the positions in the strukture and test what numbers can be used
        for x in range(len(posInt)):
            for y in range(len(posInt[0])):
                if sudoku[x][y] != '0':
                    posInt[x][y] = [sudoku[x][y]]
                    continue

                gridX = int(x / 3.0) * 3
                gridY = int(y / 3.0) * 3

                NotPossible = []

                # test all other numbers in the same sub-square
                for xOffset in range(0, 3):
                    for yOffset in range(0, 3):
                        if sudoku[gridX + xOffset][gridY + yOffset] != '0' and not sudoku[gridX + xOffset][gridY + yOffset] in NotPossible:
                            NotPossible.append(sudoku[gridX + xOffset][gridY + yOffset])

                # test all other numbers in the same row
                for xOffset in range(9):
                    if sudoku[xOffset][y] != '0' and not sudoku[xOffset][y] in NotPossible:
                        NotPossible.append(sudoku[xOffset][y])

                # test all other numbers in the same col
                for yOffset in range(9):
                    if sudoku[x][yOffset] != '0' and not sudoku[x][yOffset] in NotPossible:
                        NotPossible.append(sudoku[x][yOffset])

                # invert it so we have all the numbers that can be placed rather then all the numbers that can't be placed
                for n in range(1, 10):
                    n = str(n)
                    if not n in NotPossible:
                        posInt[x][y].append(n)

                # automaticly place a number if there is only one possible in that position
                if len(posInt[x][y]) == 1:
                    sudoku[x][y] = posInt[x][y][0]
                    Change = True

    return posInt

# solve the sudoku
def solveSudoku(sudoku):
    # get all the possible numbers
    posInt = calculatePossibleIntegers(sudoku)

    firstX = -1
    firstY = -1
    length = 42

    # place all the numbers and pick out the one with the smallest amount of possible integers to start guessing on that one
    # -- We have tested to take the longest one and that was way slower --
    for x in range(len(posInt)):
        for y in range(len(posInt[x])):
            if len(posInt[x][y]) == 0:
                return -1
            elif len(posInt[x][y]) == 1:
                sudoku[x][y] = posInt[x][y][0]
            elif len(posInt[x][y]) < length:
                firstX = x
                firstY = y
                length = len(posInt[x][y])

    # we haven't found anyone with more then one possible value
    if firstX == -1:
        return sudoku

    # guess the numbers
    for n in posInt[firstX][firstY]:
        # copy the sudoku so we have a temp copy to edit
        sudokuTemp = copyList(sudoku)
        # enter the guessed value
        sudokuTemp[firstX][firstY] = n
        # test if we get a valid solution
        saveSudoku = solveSudoku(sudokuTemp)
        # we have found a valid sudoku
        if saveSudoku != -1:
            return saveSudoku

    # there are no possible solutions to the sudoku
    return -1

# get the three-digit number in the top left corner
def CalcTopCorner(sudoku):
    saveSudoku = solveSudoku(sudoku)
    if saveSudoku == -1:
        return 0
    return int(saveSudoku[0][0] + saveSudoku[0][1] + saveSudoku[0][2])

# open the file and read the sudokus
with open(path.join(__codeDir, "external_files/pe96_sudokus.txt"), "r") as f:
    currentGrid = []
    for line in f:
        if line.startswith("Grid"):
            if currentGrid != []:
                sudokus.append(currentGrid)
            currentGrid = []
        else:
            currentGrid.append(list(line.strip()))
    sudokus.append(currentGrid)

# check that we have all 50 of the sudokus
print(len(sudokus))

# if we can use multiprocessing use that to make the process faster
if useMultithreading:
    p = Pool(4)

    solvedSudokus = p.map(CalcTopCorner, sudokus)
else:
    # do the sudokus one by one
    solvedSudokus = list(map(CalcTopCorner, sudokus))

# get the sum of all the three-digit numbers in the top-left corners of the sudokus
sum_ = 0
for n in solvedSudokus:
    sum_ += n
    print(n)

# pint the sum of the three-digit numbers
print(sum_)
