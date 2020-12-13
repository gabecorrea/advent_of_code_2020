heading_translations = {90: 'E', 180: 'S', 270: 'W', 360: 'N'}
move_instructions = [(i[0], int(i[1:])) for i in open('aoc2020/day_12/input.txt').read().splitlines()]

heading = 90
position = [0,0]
turns, moves = 0, 0
for action, amount in move_instructions:
  moves += 1
  #print(f'processing instruction number {moves}')
  #print(f'{action} for {amount}')
  if action in ['R','L']:
    debug_string = f'{heading} -> '
    turns += 1
    if action == 'R':
      heading = (heading + amount) % 360
    else: 
      heading = (heading - amount) % 360

    if heading == 0:
      heading = 360

    debug_string += f'{heading} after {action}{amount}'
    print(debug_string)
  else:
    if action == 'F':
      action = heading_translations[heading]
    
    if action == 'N':
      position[1] += amount
    elif action == 'E':
      position[0] += amount
    elif action == 'S':
      position[1] -= amount
    elif action == 'W':
      position[0] -= amount
  if position[0] < 0 or position[1] < 0:
    print(f'negative position')

print(f'Turned {turns} times')
print(abs(position[0]) + abs(position[1]))