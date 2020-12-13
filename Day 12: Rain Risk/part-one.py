with open('input.in', 'r') as input:
    directions = input.readlines()

north = 0
west = 0
angle = 0

for dir in directions:
    dirct = dir[0]
    value = int(dir[1:])
    if dirct == 'N': north += value
    elif dirct == 'S': north -= value
    elif dirct == 'W': west += value
    elif dirct == 'E': west -= value
    elif dirct == 'L': angle = (angle + value) % 360
    elif dirct == 'R': angle = (angle - value) % 360
    elif dirct == 'F':
        if angle == 0: west -= value
        elif angle == 90: north += value
        elif angle == 180: west += value
        elif angle == 270: north -= value

print(abs(north) + abs(west))
