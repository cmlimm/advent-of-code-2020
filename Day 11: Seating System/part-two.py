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
    found_seats = [False]*8
    step = 0
    width = len(layout[0])
    height = len(layout)

    while not all(found_seats):
        step += 1

        if not found_seats[0]:
            if c + step < width:
                seat = layout[r][c + step]
                if seat == '#':
                    occupied += 1
                    found_seats[0] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[0] = True
            else:
                found_seats[0] = True

        if not found_seats[1]:
            if (r + step < height) and (c + step < width):
                seat = layout[r + step][c + step]
                if seat == '#':
                    occupied += 1
                    found_seats[1] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[1] = True
            else:
                found_seats[1] = True

        if not found_seats[2]:
            if (r + step < height):
                seat = layout[r + step][c]
                if seat == '#':
                    occupied += 1
                    found_seats[2] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[2] = True
            else:
                found_seats[2] = True

        if not found_seats[3]:
            if (r + step < height) and (c - step < width):
                seat = layout[r + step][c - step]
                if seat == '#':
                    occupied += 1
                    found_seats[3] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[3] = True
            else:
                found_seats[3] = True

        if not found_seats[4]:
            if c - step < width:
                seat = layout[r][c - step]
                if seat == '#':
                    occupied += 1
                    found_seats[4] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[4] = True
            else:
                found_seats[4] = True

        if not found_seats[5]:
            if (r - step < height) and (c - step < width):
                seat = layout[r - step][c - step]
                if seat == '#':
                    occupied += 1
                    found_seats[5] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[5] = True
            else:
                found_seats[5] = True

        if not found_seats[6]:
            if (r - step < height):
                seat = layout[r - step][c]
                if seat == '#':
                    occupied += 1
                    found_seats[6] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[6] = True
            else:
                found_seats[6] = True

        if not found_seats[7]:
            if (r - step < height) and (c + step < width):
                seat = layout[r - step][c + step]
                if seat == '#':
                    occupied += 1
                    found_seats[7] = True
                elif seat == '|' or seat == '-' or seat == 'L':
                    found_seats[7] = True
            else:
                found_seats[7] = True

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
                if occupied >= 5:
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
