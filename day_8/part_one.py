instructions = open('aoc2020/day_8/input.txt').read().splitlines()
acc = 0
index = 0
executed_instructions = set()
while index not in executed_instructions:
  executed_instructions.add(index)
  op, arg = instructions[index].split(' ')
  if op == 'acc':
    acc += int(arg)
    index += 1
  elif op == 'jmp':
    index += int(arg)
  #no op
  else:
    index += 1

print(acc)