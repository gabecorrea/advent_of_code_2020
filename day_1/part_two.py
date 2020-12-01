
file = open('aoc2020/day_1/input.txt', 'r')

expenses = list(map(lambda expense: int(expense), file.read().split('\n')))
expenses.sort()

left_index, right_index = 0, -1
sum = 0
while sum != 2020:
  sum = expenses[left_index] + expenses[right_index]
  if sum > 2020:
    right_index -= 1
  elif sum < 2020:
    left_index += 1

print(expenses[left_index] * expenses[right_index])