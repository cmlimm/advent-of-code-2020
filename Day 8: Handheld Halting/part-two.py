import copy

with open('input.in', 'r') as input:
    commands = input.readlines()
    commands = [[command[:3], int(command[4:]), 0] for command in commands]
    commands.append(['END', 0, 0])

def execute(commands):
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

        if command == 'END':
            return var

isCorrect = False
for idx, repl_command in enumerate(commands):

    new_commands = copy.deepcopy(commands)

    if repl_command[0] == 'jmp':
        new_commands[idx][0] = 'nop'
    elif repl_command[0] == 'nop':
        new_commands[idx][0] = 'jmp'
    else:
        continue

    result = execute(new_commands)

    if result:
        print(result)
        break
