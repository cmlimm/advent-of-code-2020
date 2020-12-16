spoken = [17, 1, 3, 16, 19, 0]

while len(spoken) != 2020:
    last = spoken[-1]
    if last not in spoken[:-1]:
        spoken.append(0)
    else:
        reversed = spoken[::-1][1:]
        n = len(spoken)
        spoken.append(n - (n - reversed.index(last) - 1))

print(spoken[-1])
