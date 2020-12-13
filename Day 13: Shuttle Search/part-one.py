with open('input.in', 'r') as input:
    time, ids = input.readlines()
    time = int(time)
    ids = list(filter(lambda x: x != 'x', ids.split(',')))
    ids = [int(x.strip()) for x in ids]

solution = min(ids, key = lambda x: x - time % x)
print(solution*(solution - time % solution))
