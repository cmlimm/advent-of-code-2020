with open('input.in', 'r') as input:
    commands = input.readlines()
    commands = [[command[:3], int(command[4:]), 0] for command in commands]

var = 0
current = 0
while commands[current][-1] == 0:
    command = commands[current][0]
    value = commands[current][1]
    commands[current][-1] = 1

    if command == 'jmp':
        current += value

    if command == 'acc':
        var += value
        current += 1

    if command == 'nop':
        current += 1


print(var)
