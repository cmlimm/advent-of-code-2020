import re

with open('input.in', 'r') as input:
    rules = input.readlines()
    colorsRe = re.compile('(\d+)? ?(\w+ \w+) (?:bag|bags)')
    dict_rules = {}
    for rule in rules:
        colors = re.findall(colorsRe, rule)
        dict_rules[colors[0][1]] = {color: int(number) for number, color in colors[1:] if color != 'no other'}

current = {'shiny gold': 1}
result = 0

while current:
    new_current = {}
    for color, number in current.items():
        for in_color, in_number in dict_rules[color].items():
            if in_color in new_current:
                new_current[in_color] += number*in_number
            else:
                new_current[in_color] = number*in_number

    result += sum(new_current.values())
    current = new_current

print(result)
