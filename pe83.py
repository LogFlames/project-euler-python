from os import path
import itertools

code_path = path.dirname(__file__);

grid = []

class posibleWays:
    def __init__(self, startValue):
        self.startValue = startValue
        self.otherValues = []
        self.value = 0

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

    def setValue(self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value

    def getStartValue(self):
        return self.startValue

with open(path.join(code_path, "external_files/pe83_matrix.txt"), "r") as f:
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

x = 0
y = 0
while x < len(grid):
    #print(x)
    y = 0
    stayOnLevel = False
    while y < len(grid[0]):
        grid[x][y].setValue(grid[x][y].getSmallestValue())
        if x + 1 < len(grid):
            grid[x + 1][y].addOtherValue(grid[x][y].getValue())
        if y + 1 < len(grid[0]):
            grid[x][y + 1].addOtherValue(grid[x][y].getValue())
        if x - 1 >= 0 and grid[x - 1][y].getStartValue() + grid[x][y].getValue() < grid[x - 1][y].getValue():
            grid[x - 1][y].addOtherValue(grid[x][y].getValue())
            #grid[x - 1[y].setValue(grid[x - 1][y].getStartValue() + grid[x][y].getValue())
            stayOnLevel = True
        if y - 1 >= 0 and grid[x][y - 1].getStartValue() + grid[x][y].getValue() < grid[x][y - 1].getValue():
            grid[x][y - 1].addOtherValue(grid[x][y].getValue())
            y -= 2
        y += 1
    if stayOnLevel:
        x -= 1
    else:
        x += 1
    #x += 1

print(grid[len(grid) - 1][len(grid[0]) - 1].getValue())
