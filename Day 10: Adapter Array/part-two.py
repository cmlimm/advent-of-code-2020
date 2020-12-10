with open('input.in', 'r') as input:
    ratings = input.readlines()
    ratings = [int(rating) for rating in ratings]

ratings = sorted(ratings)
ratings.insert(0, 0)
end = len(ratings)
paths = [0]*end
for idx, adapter in enumerate(ratings):
    if idx == 0 or idx == 1:
        paths[idx] = 1
    elif idx == 2:
        paths[2] = 1 + (ratings[2] - ratings[0] <= 3)
    else:
        for idx_bf, adapter_bf in enumerate(ratings[idx - 3:idx]):
            if adapter - adapter_bf <= 3:
                paths[idx] += paths[idx + idx_bf - 3]

print(paths[-1])
