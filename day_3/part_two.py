from functools import reduce

grid = open('aoc2020/day_3/input.txt', 'r').read().split('\n')
pattern_boundary = len(grid[0]) - 1
bottom_row = len(grid) - 1

def damn_the_trees_full_speed_ahead(slope):
  x, y = slope[0], slope[1]
  num_trees = 0
  while(y <= bottom_row):
    if x in range(pattern_boundary + 1, pattern_boundary + slope[0] + 1):
      # rollover
      x -= pattern_boundary + 1
    
    if grid[y][x] == '#':
      num_trees += 1

    x += slope[0]
    y += slope[1]
  print(num_trees)
  return num_trees

test_slopes = [
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2),
]

# I have since learned about math.prod available since python 3.8 but whatever
print(reduce( lambda x, y: x * y, list(map(lambda slope: damn_the_trees_full_speed_ahead(slope), test_slopes))))