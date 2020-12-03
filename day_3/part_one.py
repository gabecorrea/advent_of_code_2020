grid = open('aoc2020/day_3/input.txt', 'r').read().split('\n')
pattern_boundary = len(grid[0]) - 1
bottom_row = len(grid) - 1
x, y = 3, 1
num_trees = 0
while(y <= bottom_row):
  if x in range(pattern_boundary+1, pattern_boundary+4):
    # rollover
    x -= pattern_boundary + 1
  
  if grid[y][x] == '#':
    num_trees += 1

  x += 3
  y += 1

print(num_trees)