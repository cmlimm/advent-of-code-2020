with open('input.in', 'r') as input:
    boarding_passes = input.readlines()

def get_id(boarding_pass):
    row_instr = boarding_pass[:7]
    column_instr = boarding_pass[7:]

    lower = 0
    upper = 127

    for letter in row_instr:
        if letter == 'F':
            upper = lower + (upper - lower) // 2
        if letter == 'B':
            lower = lower + (upper - lower) // 2 + 1

    row = lower

    lower = 0
    upper = 7

    for letter in column_instr:
        if letter == 'L':
            upper = lower + (upper - lower) // 2
        if letter == 'R':
            lower = lower + (upper - lower) // 2 + 1

    column = lower
    return row*8 + column

solution = max(boarding_passes, key=lambda x: get_id(x))

print(get_id(solution))
