instruction_sequence = [(s.split(' ')[0], s.split(' ')[1]) for s in open('aoc2020/day_8/input.txt').read().splitlines()]

def flip_instruction(instruction):
  operation, arg = instruction
  if operation == 'jmp':
    return ('nop', arg)
  elif operation == 'nop':
    return ('jmp', arg)
  else:
    return (operation, arg)

def boot_me_up(instruction_sequence):
  acc, index = 0, 0
  executed_instructions = set()
  while index < len(instruction_sequence):
    if index in executed_instructions:
      return False
    executed_instructions.add(index)
    op, arg = instruction_sequence[index]
    if op == 'acc':
      acc += int(arg)
      index += 1
    elif op == 'jmp':
      index += int(arg)
    #no op
    else:
      index += 1

  if index == len(instruction_sequence):
    return acc
  else:
    #print(len(executed_instructions))
    return False

for i in range(len(instruction_sequence) - 1):
  instruction_sequence[i] = flip_instruction(instruction_sequence[i])
  if result := boot_me_up(instruction_sequence):
    print(result)
  else:
    instruction_sequence[i] = flip_instruction(instruction_sequence[i])  
