from collections import defaultdict

seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input.txt').read().splitlines()]
print(len(seat_grid))
seat_grid.insert(0, list('.' * 97))
seat_grid.append(list('.' * 97))

new_grid = [list('.' * 97)]
new_grid.append(list('.' * 97))

for r in range(1,len(seat_grid)-1):
  row = seat_grid[r]
  for c in range(1,len(row)-1):
    seat = row[c]
    if seat == 'L':
      seat_grid[r][c] = '#'

iterations = 0
while True:
  visible_seats = defaultdict(lambda: set())
  print(iterations)
  # pass 1, top down left right
  for r in range(1,len(seat_grid)-1):
    row = seat_grid[r]
    for c in range(1,len(row)-1):
      seat = row[c]
      # north
      if seat == '#' or 'N' in visible_seats[(r-1,c)]:
        visible_seats[(r+1,c)].add('N')
      
      # west
      if seat == '#' or 'W' in visible_seats[(c-1, r)]:
        visible_seats[(r,c+1)].add('W')
      
      # northwest
      if seat == '#' or 'NW' in visible_seats[(c-1, r-1)]:
        visible_seats[(r+1,c+1)].add('NW')

  #pass 2, bottom up left right
  for r in range(len(seat_grid)-1,1,-1):
    row = seat_grid[r]
    for c in range(1,len(row)-1):
      seat = row[c]
      if seat == '#' or 'S' in visible_seats[(r+1, c)]:
        visible_seats[(r-1, c)].add('S')
      
      if seat == '#' or 'SW' in visible_seats[(r+1, c-1)]:
        visible_seats[(r-1,c+1)].add('SW')
      
      # if seat == '#' or 'W' in visible_seats[(r, c-1)]:
      #   visible_seats[(r,c+1)].add('W')

  #pass 3, top down, right to left 
  for r in range(1,len(seat_grid)-1):
    row = seat_grid[r]
    for c in range(len(row)-1, 1, -1):
      seat = row[c]
      # East
      if seat == '#' or 'E' in visible_seats[(r,c+1)]:
        visible_seats[(r, c-1)].add('E')
        
      if seat == '#' or 'NE' in visible_seats[(r+1,c+1)]:
        visible_seats[(r+1,c-1)].add('NE')

  # pass 4 bottom up, right to left
  for r in range(len(seat_grid)-1,1,-1):
    row = seat_grid[r]
    for c in range(len(row)-1, 1, -1):
      seat = row[c]
      # SE
      if seat == '#' or 'E' in visible_seats[(r+1,c+1)]:
        visible_seats[(r-1, c-1)].add('SE')


  new_grid = [list('.' * 97)]
  new_grid.append(list('.' * 97))
  
  #assign_seats
  for r in range(1,len(seat_grid)-1):
    row = seat_grid[r]
    new_row = []
    for c in range(1,len(row)-1):
      seat = row[c]
      visible_seat_count = len(visible_seats[(r,c)])

      if seat != '.':
        if visible_seat_count >= 5:
          new_row.append('L')
        else:
          new_row.append('#')
      else:
        new_row.append('.')

    new_grid.insert(r, ['.'] + new_row + ['.'])
  iterations += 1

  if seat_grid == new_grid:
    break
  else: 
    seat_grid = new_grid

occupied_seat_count = len([seat for seat_row in seat_grid for seat in seat_row if seat == '#'])
print(occupied_seat_count)