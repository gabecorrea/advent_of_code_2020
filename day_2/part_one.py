import re
# parse input into list of tuples of:
  # range object
  # haystack
  # test string

# use list comprehension if possible
  # not too important

def process_input_lines(line):
  regex = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')
  m = regex.match(line)
  l_bound, u_bound, target, password = int(m.group(1)), int(m.group(2))+1, m.group(3), m.group(4)
  return (range(l_bound,u_bound), target, password)

file = open('aoc2020/day_2/input.txt', 'r')
candidate_tuples = list(map(process_input_lines, file.read().split('\n')))
valid_passwords = [candidate for candidate in candidate_tuples if candidate[2].count(candidate[1]) in candidate[0]]
print(len(valid_passwords))