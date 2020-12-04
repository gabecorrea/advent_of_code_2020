import re

def field_list_to_dict(field_list):
  k,v = zip(*(field.split(':') for field in field_list))
  return dict(zip(k,v))

def validate_passport(passport):
  field_checks = []

  if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
    field_checks.append(True)
  else:
    return False
  
  height_check = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
  if height_check:
    if height_check.group(2) == 'cm' and int(height_check.group(1)) in range(150, 194):
      field_checks.append(True)
    elif height_check.group(2) == 'in' and int(height_check.group(1)) in range(59, 77):
      field_checks.append(True)
    else:
      return False
  else:
    return False

  if re.match('^#([0-9a-f]){6}$', passport['hcl']):
    field_checks.append(True)
  else:
    return False

  if re.match('^[0-9]{9}$', passport['pid']):
    field_checks.append(True)
  else:
    return False

  try:
    if int(passport['byr']) in range(1920,2003) \
    and int(passport['iyr']) in range(2010,2021) \
    and int(passport['eyr']) in range(2020,2031):
      field_checks.append(True)
    else:
      return False
  except ValueError:
    return False
  
  if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    field_checks.append(True)
  else:
    return False

  if all(field_checks):
    return True
  else:
    return False

passport_list = [re.split(' |\n', passport_string) for passport_string in open('aoc2020/day_4/input.txt', 'r').read().split('\n\n')]
candidate_passports = [passport_data for passport_data in passport_list if len(passport_data) >= 7]
passport_dicts = list(map(field_list_to_dict,candidate_passports))
validate_passports = [validate_passport(passport) for passport in passport_dicts]

print(len(list(filter(None, validate_passports))))