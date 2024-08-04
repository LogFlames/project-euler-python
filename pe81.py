from os import path
import itertools

code_path = path.dirname(__file__);

grid = []

miniValue = -1

class posibleWays:
    def __init__(self, startValue):
        self.startValue = startValue
        self.otherValues = []

    def addOtherValue(self, otherValue):
        self.otherValues.append(otherValue)

    def getSmallestValue(self):
        if len(self.otherValues) <= 0:
            return self.startValue
        smallestValue = self.otherValues[0]
        for n in self.otherValues:
            if n < smallestValue:
                smallestValue = n
        return smallestValue + self.startValue

with open(path.join(code_path, "external_files/pe81_matrix.txt"), "r") as f:
    for line in f:
        toAppendToGrid = []
        nextInt = ""
        for char in line.strip():
            if char == ",":
                toAppendToGrid.append(posibleWays(int(nextInt)))
                nextInt = ""
            else:
                nextInt += char
        toAppendToGrid.append(posibleWays(int(nextInt)))
        grid.append(toAppendToGrid)

for x in range(len(grid)):
    for y in range(len(grid[0])):
        grid[x][y] = grid[x][y].getSmallestValue()
        if x + 1 < len(grid):
            grid[x + 1][y].addOtherValue(grid[x][y])
        if y + 1 < len(grid[0]):
            grid[x][y + 1].addOtherValue(grid[x][y])

print(grid[len(grid) - 1][len(grid[0]) - 1])
