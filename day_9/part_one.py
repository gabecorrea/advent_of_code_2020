numbers = [int(n) for n in open('aoc2020/day_9/input.txt').read().splitlines()]
print(len(numbers))
for index in range(26,len(numbers)):
  test = numbers[index]
  for first in range(index-26, index):
    for second in range(index-25, index):
      #print(f'{test} | {numbers[first]} {numbers[second]} | {numbers[first] + numbers[second]}')
      
      if test - numbers[first] == numbers[second]:
        print(f'found a match for: {test}:{first},{second}')
        break
    else:
      continue
    break
  else:
    print('this should mean both all numbers in set failed.')
    continue
  print('here I am')
  continue

print('what is this')