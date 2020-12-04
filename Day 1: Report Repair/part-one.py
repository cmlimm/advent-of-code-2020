with open('input.in', 'r') as input:
    expenses = []
    for line in input.readlines():
        expenses.append(int(line))

for number in expenses:
    if 2020 - number in expenses:
        solution = number*(2020 - number)
        break

print(solution)
