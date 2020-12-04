import re

passport_list = [re.split(' |\n', passport_string) for passport_string in open('aoc2020/day_4/input.txt', 'r').read().split('\n\n')]
candidate_passports_as_list = [passport_data for passport_data in passport_list if len(passport_data) >= 7]

valid_count = 0
for candidate in candidate_passports_as_list:
  if len(candidate) == 7:
    for field in candidate:
      if field.find('cid:') != -1:
        break
    else:
      valid_count += 1
  else:
    valid_count += 1

print(valid_count)