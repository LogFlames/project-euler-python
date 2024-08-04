from os import path

code_path = path.dirname(__file__)

# all numbers we can create in order (following the rules)
rome_numbers = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

# convert a rome nubmer to normal numbers
def getValue(sym):
    for n in rome_numbers:
        if n[0] == sym:
            return n[1]
    return -1

# convert a normal number to rome numbers
def getSym(num):
    for n in rome_numbers:
        if n[1] == num:
            return n[0]
    return ""

numbers = []
charactersUsed = 0

# laod the file with all the rome numbers and convert them to normal numbers
with open(path.join(code_path, "external_files/pe89_numbers.txt"), "r") as f:
    for line in f:
        line = line.strip()
        num = 0
        symInd = 0
        charactersUsed += len(line)
        while symInd < len(line):
            if symInd + 1 < len(line) and getValue(line[symInd + 1]) > getValue(line[symInd]):
                num += (getValue(line[symInd + 1]) - getValue(line[symInd]))
                symInd += 1
            else:
                num += getValue(line[symInd])
            symInd += 1
        numbers.append(num)

length = 0

# go thru all the normal numbers and save the length of the shortest representation of the number in rome numbers
for num in numbers:
    rome_num_short = ""
    for rome_number in rome_numbers:
        while num - rome_number[1] >= 0:
            rome_num_short += rome_number[0]
            num -= rome_number[1]

    length += len(rome_num_short)
    print(rome_num_short)

# print the amount of letters used and how many was in the file
print(length)
print(charactersUsed)
print("")
# print how many letters shorter the new version if over the old one
print(charactersUsed - length)
