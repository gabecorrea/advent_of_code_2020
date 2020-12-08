bag_rules = open('aoc2020/day_7/input.txt').read().split('\n')
possibilities = dict()
for rule in bag_rules:
  if rule.find('no other bags') != -1:
    continue

  enclosing_rule, contained_rules = rule.split('contain')
  enclosing_color = enclosing_rule[:enclosing_rule.find(' bag')]

  # build list of tuples with bag color and quantity
  contained_bag_colors = [(s[2:s.find(' bag')].strip(), s[1]) for s in contained_rules.split(',')]
  #print(contained_bag_colors)
  possibilities[enclosing_color] = contained_bag_colors

required_bags = ['shiny gold']
stack = []
stack.extend(possibilities.get('shiny gold'))
while len(stack) > 0:
  bag_info = stack.pop()
  enclosed_bags = possibilities.get(bag_info[0])
  if enclosed_bags:
    stack.extend(enclosed_bags * int(bag_info[1]))
    for i in range(int(bag_info[1])):
      required_bags.append(bag_info[0])

bag_count = 0
for bag in required_bags:
  if contained_bags := possibilities.get(bag):
    bag_count += sum(int(t[1]) for t in contained_bags)
  else:
    bag_count += 1

print(bag_count)