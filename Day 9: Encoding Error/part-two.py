import itertools

with open('input.in', 'r') as input:
    numbers = input.readlines()
    numbers = [int(number) for number in numbers]

def isSum(numbers, sum):
    n = len(numbers)

    for i in range(0, n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == sum:
                return True

    return False

for idx, number in enumerate(numbers[25:]):
    if not isSum(numbers[idx:idx + 25], number):
        error = number
        break

acc = list(itertools.accumulate(numbers, lambda x, y: x + y))
for idx, number in enumerate(numbers):
    acc = list(map(lambda x: x - number, acc))
    if error in acc:
        error_idx = acc.index(error)
        start = idx + 1
        end = error_idx + 1
        break

minimum = min(numbers[start:end])
maximum = max(numbers[start:end])
print(minimum + maximum)
