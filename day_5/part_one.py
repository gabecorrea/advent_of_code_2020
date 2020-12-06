boarding_codes = open('aoc2020/day_5/input.txt').read().split('\n')

def find_seat_position(boarding_code, possible_values):
  code = boarding_code.pop(0)
  position = 0

  if len(possible_values) == 2:
    return possible_values[0] if code in ['F','L'] else possible_values[1]
  
  mid = int(len(possible_values) / 2)
  if code in ['F','L']:
    position = find_seat_position(boarding_code, possible_values[:mid])
  else:
    position = find_seat_position(boarding_code, possible_values[mid:])

  return position

seat_rows = [ 
  find_seat_position(list(x)[:7], list(range(0,128))) for x in boarding_codes
]

seat_cols = [
  find_seat_position(list(x)[7:], list(range(0,8))) for x in boarding_codes
]

print(max([seat_rows[i] * 8 + seat_cols[i] for i in range(len(seat_rows))]))