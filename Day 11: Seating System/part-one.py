import copy

with open('input.in', 'r') as input:
    layout = input.readlines()

def make_frame(layout):
    n = len(layout[0])
    layout = ['|' + row.strip() + '|' for row in layout]
    layout.insert(0, '-'*(n + 1))
    layout.append('-'*(n + 1))

    layout = [list(row) for row in layout]

    return layout

def count_adjacent_occupied(r, c, layout):
    occupied = 0
    if layout[r][c + 1] == '#':
        occupied += 1
    if layout[r + 1][c + 1] == '#':
        occupied += 1
    if layout[r + 1][c] == '#':
        occupied += 1
    if layout[r + 1][c - 1] == '#':
        occupied += 1
    if layout[r][c - 1] == '#':
        occupied += 1
    if layout[r - 1][c - 1] == '#':
        occupied += 1
    if layout[r - 1][c] == '#':
        occupied += 1
    if layout[r - 1][c + 1] == '#':
        occupied += 1

    return occupied

def change_seats(framed):
    new_framed = copy.deepcopy(framed)
    for idx_row, row in enumerate(framed):
        for idx_column, seat in enumerate(row):
            if seat == 'L':
                occupied = count_adjacent_occupied(idx_row, idx_column, framed)
                if occupied == 0:
                    new_framed[idx_row][idx_column] = '#'
            if seat == '#':
                occupied = count_adjacent_occupied(idx_row, idx_column, framed)
                if occupied >= 4:
                    new_framed[idx_row][idx_column] = 'L'
    return new_framed

framed = make_frame(layout)
new_framed = change_seats(framed)

while framed != new_framed:
    framed = new_framed
    new_framed = change_seats(framed)

occupied = 0
for row in framed:
    occupied += row.count('#')
print(occupied)
