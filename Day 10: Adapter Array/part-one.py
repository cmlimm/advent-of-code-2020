import itertools

with open('input.in', 'r') as input:
    ratings = input.readlines()
    ratings = [int(rating) for rating in ratings]

ratings = sorted(ratings)
pairs = list(zip(ratings, ratings[1:]))
diff = list(map(lambda x: x[1] - x[0], pairs))
# print(pairs)
# print(diff)
# print(dict(zip(pairs, diff)))
# print(ratings)
print((diff.count(3) + 1)*(diff.count(1) + 1))
