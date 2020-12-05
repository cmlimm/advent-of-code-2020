with open('input.in', 'r') as input:
    passports = input.read().split('\n\n')

valid = 0
for passport in passports:
    if 'byr:' in passport and \
       'iyr:' in passport and \
       'eyr:' in passport and \
       'hgt:' in passport and \
       'hcl:' in passport and \
       'ecl:' in passport and \
       'pid:' in passport:
       valid += 1

print(valid)
