from itertools import starmap
import re

with open('input.in', 'r') as input:
    instructions = input.readlines()

maskRe = re.compile('mask = ((?:0|1|X)+)')
memRe = re.compile('mem\[(\d+)\] = (\d+)')

def apply_mask(number, mask):
    number = format(number, '036b')
    res = list(starmap(lambda x, y: y if x != y and y != 'X' else x, zip(number, mask)))

    return int(''.join(res), 2)

memory = {}

for instruction in instructions:
    if mask_cmd := re.match(maskRe, instruction):
        mask = mask_cmd.group(1)
    if memory_cmd := re.match(memRe, instruction):
        number = int(memory_cmd.group(2))
        memory[memory_cmd.group(1)] = apply_mask(number, mask)

print(sum(memory.values()))
