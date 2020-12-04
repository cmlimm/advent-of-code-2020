with open('input.in', 'r') as input:
    treeMap = []
    for line in input.readlines():
        treeMap.append(line.strip())

x, y = 0, 0
height = len(treeMap)
width = len(treeMap[0])
treeCounter = 0

while y != height - 1:
    x = (x + 3) % width
    y += 1

    if treeMap[y][x] == '#':
        treeCounter += 1

print(treeCounter)
