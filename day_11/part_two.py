from collections import defaultdict

seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input.txt').read().splitlines()]
#seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input_sparse.txt').read().splitlines()]
#seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input_none.txt').read().splitlines()]
#seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input_initial.txt').read().splitlines()]
print(len(seat_grid))
pad_count = len(seat_grid) + 2
seat_grid.insert(0, list('.' * pad_count))
seat_grid.append(list('.' * pad_count))

new_grid = [list('.' * pad_count)]
new_grid.append(list('.' * pad_count))

iterations = 0

while True:
  visible_seats = defaultdict(lambda: set())
  #print(iterations)
  # pass 1, top down left right
  for r in range(1,len(seat_grid)-1):
    row = seat_grid[r]
    # left to right
    for c in range(1,len(row)-1):
      seat = row[c]
      # setting south, east, and southeast
      if seat == '.':
        if 'N' in visible_seats[(r,c)]:
          visible_seats[(r+1,c)].add('N')

        if 'W' in visible_seats[(r,c)]:
          visible_seats[(r,c+1)].add('W')

        if 'NW' in visible_seats[(r,c)]:
          visible_seats[(r+1,c+1)].add('NW')

      elif seat == '#':
        visible_seats[(r+1,c)].add('N')
        visible_seats[(r,c+1)].add('W')
        visible_seats[(r+1,c+1)].add('NW')
    
    # right to left
    for c in range(len(row)-2, 1, -1):
      seat = row[c]
      # setting west and southwest
      if seat == '.':
        if 'E' in visible_seats[(r,c)]:
          visible_seats[(r, c-1)].add('E')
        if 'NE' in visible_seats[(r,c)]:
          visible_seats[(r+1,c-1)].add('NE')
      elif seat == '#':
        visible_seats[(r, c-1)].add('E')
        visible_seats[(r+1,c-1)].add('NE')

  #pass 2, bottom up, left to right
  for r in range(len(seat_grid)-2,1,-1):
    row = seat_grid[r]
    for c in range(1,len(row)-1):
      seat = row[c]
      # setting north and northeast
      if seat == '.':
        if 'S' in visible_seats[(r,c)]:
          visible_seats[(r-1, c)].add('S')
        if 'SW' in visible_seats[(r,c)]:
          visible_seats[(r-1, c+1)].add('SW')
      elif seat == '#':
        visible_seats[(r-1, c)].add('S')
        visible_seats[(r-1, c+1)].add('SW')

    # right to left
    for c in range(len(row)-2, 1, -1):
      seat = row[c]

      # setting northwest
      if seat == '.' and 'SE' in visible_seats[(r,c)]:
        visible_seats[(r-1, c-1)].add('SE')
      elif seat == '#':
        visible_seats[(r-1, c-1)].add('SE')

  new_grid = [list('.' * pad_count)]
  new_grid.append(list('.' * pad_count))
  
  # last row messing up somehow.
  # maybe make that print grid method
  # assign_seats
  for r in range(1,len(seat_grid)-1):
    row = seat_grid[r]
    new_row = []
    for c in range(1,len(row)-1):
      seat = row[c]
      visible_occupied_seat_count = len(visible_seats[(r,c)])

      if seat != '.':
        if seat == '#' and visible_occupied_seat_count >= 5:
          new_row.append('L')
        elif seat == 'L' and visible_occupied_seat_count == 0:
          new_row.append('#')
        else:
          new_row.append(seat)
      else:
        new_row.append('.')

    new_grid.insert(r, ['.'] + new_row + ['.'])
  iterations += 1

  if seat_grid == new_grid:
    break
  else: 
    seat_grid = new_grid

occupied_seat_count = len([seat for seat_row in seat_grid for seat in seat_row if seat == '#'])
print('-----')
print(occupied_seat_count)