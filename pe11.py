from os import path

code_path = path.dirname(__file__)

grid = []

with open(path.join(code_path, "external_files/pe11_grid.txt"), "r") as f:
    for line in f:
        gridNextLineObject = []
        toAppendToGridNextLineObject = ""
        for char in line:
            if char == ".":
                gridNextLineObject.append(int(toAppendToGridNextLineObject))
                toAppendToGridNextLineObject = ""
            else:
                toAppendToGridNextLineObject += char
        grid.append(gridNextLineObject)

highestProduct = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if x + 3 < len(grid):
            value = grid[x][y] * grid[x + 1][y] * grid[x + 2][y] * grid[x + 3][y]
            if value > highestProduct:
                highestProduct = value
        if y + 3 < len(grid[0]):
            value = grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
            if value > highestProduct:
                highestProduct = value
        if x + 3 < len(grid) and y + 3 < len(grid[0]):
            value = grid[x][y] * grid[x + 1][y + 1] * grid[x + 2][y + 2] * grid[x + 3][y + 3]
            if value > highestProduct:
                highestProduct = value
        if x - 3 >= 0 and y + 3 < len(grid[0]):
            value = grid[x][y] * grid[x - 1][y + 1] * grid[x - 2][y + 2] * grid[x - 3][y + 3]
            if value > highestProduct:
                highestProduct = value

print(highestProduct)
