from itertools import starmap
from itertools import product
import re

with open('input.in', 'r') as input:
    instructions = input.readlines()

maskRe = re.compile('mask = ((?:0|1|X)+)')
memRe = re.compile('mem\[(\d+)\] = (\d+)')

def apply_mask(number, mask):
    number = format(number, '036b')
    res = list(starmap(lambda x, y: y if y != '0' else x, zip(number, mask)))

    return ''.join(res)

def get_addresses(floating_address):
    n_floating = floating_address.count('X')
    combinations = product([0, 1], repeat = n_floating) # get all possible X replacement pattern

    addresses = []
    for combination in combinations:
        counterX = -1
        adr = floating_address

        # for each X replacement pattern we enumerate over address with X's in it
        # and replace each X character with corresponding 0 or 1 from patter
        # example of iterations:
        # x x x x -> 1 x x x -> 1 0 x x -> 1 0 1 x -> 1 0 1 0
        for idx, chr in enumerate(floating_address):
            if chr == 'X':
                counterX += 1
                adr = adr[:idx] + str(combination[counterX]) + adr[idx + 1:]
        addresses.append(int(adr, 2))

    return addresses

memory = {}

for instruction in instructions:
    if mask_cmd := re.match(maskRe, instruction):
        mask = mask_cmd.group(1)
    if memory_cmd := re.match(memRe, instruction):
        number = int(memory_cmd.group(1)) # str to number
        addresses = get_addresses(apply_mask(number, mask)) # get all possible memory addresses
        for address in addresses:
            memory[address] = int(memory_cmd.group(2))

print(sum(memory.values()))
