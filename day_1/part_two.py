from functools import reduce

file = open('aoc2020/day_1/input.txt', 'r')

expenses = list(map(lambda expense: int(expense), file.read().split('\n')))
expenses.sort()

for x in expenses:
  for y in expenses[1::]:
    for z in expenses[2::]:
      if x + y + z == 2020:
        print(x * y * z)
        break
    else:
      continue
    break
  else:
    continue
  break
