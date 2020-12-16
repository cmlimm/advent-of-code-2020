from collections import Counter

spoken = Counter({17: 1, 1: 2, 3: 3, 16: 4, 19: 5})
turn = 6
last = 0

while turn != 30000000:
    if spoken[last] == 0:
        spoken[last] = turn
        last = 0
    else:
        spoken[last], last = turn, turn - spoken[last]
    turn += 1

print(last)
