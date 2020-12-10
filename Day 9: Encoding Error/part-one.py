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
        print(number)
        break
