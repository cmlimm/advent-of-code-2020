with open('input.in', 'r') as input:
    time, ids = input.readlines()
    time = int(time)
    ids = [(idx, int(bus.strip())) for idx, bus in enumerate(ids.split(',')) if bus != 'x']


time = 0
step = 1

for offset, bus in ids:
    while (offset + time) % bus:
        time += step
    step *= bus

print(time)
