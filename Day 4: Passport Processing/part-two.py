import re

with open('input.in', 'r') as input:
    passports = input.read().split('\n\n')

byrRe = re.compile('byr:(19[2-9][0-9]|200[0-2])( |\n|$)')
iyrRe = re.compile('iyr:(201[0-9]|2020)( |\n|$)')
eyrRe = re.compile('eyr:(202[0-9]|2030)( |\n|$)')
hgtRe = re.compile('hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)( |\n|$)')
hclRe = re.compile('hcl:#[0-9a-f]{6}( |\n|$)')
eclRe = re.compile('ecl:(amb|blu|brn|gry|grn|hzl|oth)( |\n|$)')
pidRe = re.compile('pid:\d{9}( |\n|$)')

valid = 0
for passport in passports:
    if re.search(byrRe, passport) and \
       re.search(iyrRe, passport) and \
       re.search(eyrRe, passport) and \
       re.search(hgtRe, passport) and \
       re.search(hclRe, passport) and \
       re.search(eclRe, passport) and \
       re.search(pidRe, passport):
       valid += 1

print(valid)
