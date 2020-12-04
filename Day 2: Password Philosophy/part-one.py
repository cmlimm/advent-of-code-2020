counter = 0

with open('input.in', 'r') as input:
    for line in input.readlines():
        number, letter, password = line.split()

        number = [int(x) for x in number.split('-')]
        letter = letter[0]

        if number[0] <= password.count(letter) <= number[1]:
            counter += 1

print(counter)
