from functools import reduce

with open('input.in', 'r') as input:
    directions = input.readlines()

waypoint = complex(10, 1)
ship = complex(0, 0)

for dir in directions:
    dirct = dir[0]
    value = int(dir[1:])
    if dirct == 'N': waypoint += complex(0, value)
    elif dirct == 'S': waypoint += complex(0, -value)
    elif dirct == 'E': waypoint += complex(value, 0)
    elif dirct == 'W': waypoint += complex(-value, 0)
    elif dirct == 'L':
        for _ in range(value // 90):
            waypoint = complex(-waypoint.imag, waypoint.real)
    elif dirct == 'R':
        for _ in range(value // 90):
            waypoint = complex(waypoint.imag, -waypoint.real)
    elif dirct == 'F': ship += waypoint*value

print(abs(ship.real) + abs(ship.imag))
