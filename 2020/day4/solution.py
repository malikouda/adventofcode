import re

with open('./input.txt', 'r') as f:
    all_text = f.read()
    passports = all_text.strip().split('\n\n')

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

count = 0
for i, p in enumerate(passports):
    passports[i] = p.replace('\n', ' ')
    passports[i] = passports[i].split()
    passports[i] = dict([tuple(field.split(':')) for field in passports[i]])
    keys = set(passports[i].keys())
    if not required.issubset(keys): continue
    passport = passports[i]
    if len(passport['byr']) != 4 or int(passport['byr']) not in range(1920, 2003): continue
    if len(passport['iyr']) != 4 or int(passport['iyr']) not in range(2010, 2021): continue
    if len(passport['eyr']) != 4 or int(passport['eyr']) not in range(2020, 2031): continue
    hgt = passport['hgt']
    if hgt[-2:] != 'cm' and hgt[-2:] != 'in': continue
    elif hgt[-2:] == 'cm' and int(hgt[:-2]) not in range(150, 194): continue
    elif hgt[-2:] == 'in' and int(hgt[:-2]) not in range(59, 77): continue
    regex = '^#[a-f0-9]{6}$'
    if not bool(re.match(regex, passport['hcl'])): continue
    if passport['ecl'] not in valid_ecl: continue
    if len(passport['pid']) != 9: continue
    try:
        int(passport['pid'])
    except Exception as e:
        continue
    count += 1

print(count)
    
