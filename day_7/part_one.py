bag_rules = open('aoc2020/day_7/input.txt').read().split('\n')
possibilities = dict()
for rule in bag_rules:
  enclosing_rule, contained_rules = rule.split('contain')
  enclosing_color = enclosing_rule[:enclosing_rule.find(' bag')]
  contained_bag_colors = [s[2:s.find(' bag')] for s in contained_rules.split(',')]
  print(contained_bag_colors)
  for color in contained_bag_colors:
    containing_list = possibilities.get(color.strip(), [])
    containing_list.append(enclosing_color)
    possibilities[color.strip()] = containing_list

enclosing_bags = set()
stack = []
stack.extend(possibilities.get('shiny gold'))
enclosing_bags.update(possibilities.get('shiny gold'))
while len(stack) > 0:
  bag = stack.pop()
  if possibilities.get(bag):
    stack.extend(possibilities.get(bag))
    enclosing_bags.update(possibilities.get(bag))
  else:
    enclosing_bags.add(bag)

print(len(enclosing_bags))