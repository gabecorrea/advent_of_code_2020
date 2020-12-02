import re
# use regex to split out parts of input line and return a list of tuples.
# use a list comprehension to return valid passwords from tuple list
# the positional reference to tuple elements got a little awkward for this part, so could switch to named tuples if it mattered.

def process_input_lines(line):
  regex = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')
  m = regex.match(line)
  pos_1, pos_2, target, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
  return (int(pos_1)-1, int(pos_2)-1, target, password)

file = open('aoc2020/day_2/input.txt', 'r')
candidate_tuples = list(map(process_input_lines, file.read().split('\n')))

# ^ operator is XOR for booleans in python
valid_passwords = [candidate for candidate in candidate_tuples if ((candidate[3][candidate[0]] == candidate[2]) ^ (candidate[3][candidate[1]] == candidate[2]))]
print(len(valid_passwords))