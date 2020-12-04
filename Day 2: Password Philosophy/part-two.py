counter = 0

with open('input.in', 'r') as input:
    for line in input.readlines():
        number, letter, password = line.split()

        number = [int(x) for x in number.split('-')]
        letter = letter[0]

        isOnFirstPosition = password[number[0] - 1] == letter
        isOnSecondPosition = password[number[1] - 1] == letter
        if bool(isOnFirstPosition) ^ bool(isOnSecondPosition):
            counter += 1

print(counter)
