import re

with open('input.in', 'r') as input:
    rules = input.readlines()
    colorsRe = re.compile('(\w+ \w+) bag')
    dict_rules = {}
    for rule in rules:
        colors = re.findall(colorsRe, rule)
        dict_rules[colors[0]] = set(colors[1:])

current = {'shiny gold'}
bags = []

while current:
    new_current = set()
    counter = 0
    for key, value in dict_rules.items():
        if current.intersection(value):
            new_current.add(key)
            bags.append(key)
            counter += 1

    if counter != 0:
        for bag in bags[-counter:]:
            dict_rules.pop(bag)

    current = new_current

print(len(bags))
