with open('input.in', 'r') as input:
    treeMap = []
    for line in input.readlines():
        treeMap.append(line.strip())

height = len(treeMap)
width = len(treeMap[0])

r1d1 = [treeMap[y][y % width] for y in range(height)].count('#')
r3d1 = [treeMap[y][3*y % width] for y in range(height)].count('#')
r5d1 = [treeMap[y][5*y % width] for y in range(height)].count('#')
r7d1 = [treeMap[y][7*y % width] for y in range(height)].count('#')
r1d2 = [treeMap[y][y // 2 % width] for y in range(0, height, 2)].count('#')

print(r1d1*r3d1*r5d1*r7d1*r1d2)
