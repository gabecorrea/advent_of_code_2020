# pad seat_grid with exterior floor space to remove boundary checking logic
seat_grid = [['.'] + list(row) + ['.'] for row in open('aoc2020/day_11/input.txt').read().splitlines()]
print(len(seat_grid))
seat_grid.insert(0, list('.' * 97))
seat_grid.append(list('.' * 97))
# brutish and hopefully short, but not too nasty
# one row at a time
# for each seat pull out filtered slices of 3 seats above, two adjacent seats, and 3 seats below and count em.
  # handle range boundaries
# build new row of seats and append to grid
# replace grid at end
iterations = 0
while True:
  #if iterations % 100 == 0:
  print(iterations)
  new_grid = [list('.' * 97)]
  new_grid.append(list('.' * 97))
  for i in range(1,len(seat_grid)-1):
    new_row = []
    row = seat_grid[i]
    for ii in range(1,len(row)-1):
      seat = row[ii]
      neighbor_count = 0
      neighbor_count += len([s for s in seat_grid[i-1][ii-1:ii+2] if s == '#'])
      if row[ii-1] == '#':
        neighbor_count += 1
      if row[ii+1] == '#':
        neighbor_count += 1
      neighbor_count += len([s for s in seat_grid[i+1][ii-1:ii+2] if s == '#'])
      
      if seat == 'L' and neighbor_count == 0:
        new_row.append('#')
      elif seat == '#' and neighbor_count >= 4:
        new_row.append('L')
      else:
        new_row.append(seat)
    new_grid.insert(i, ['.'] + new_row + ['.'])
  if seat_grid == new_grid:
    break
  else:
    seat_grid = new_grid
  
  iterations += 1

occupied_seat_count = len([seat for seat_row in seat_grid for seat in seat_row if seat == '#'])
print(occupied_seat_count)