with open('input.in', 'r') as input:
    expenses = []
    for line in input.readlines():
        expenses.append(int(line))

for first_number in expenses:
    diff2020 = 2020 - first_number
    for second_number in expenses:
        if diff2020 - second_number in expenses:
            solution = first_number*second_number*(2020 - first_number - second_number)

print(solution)
