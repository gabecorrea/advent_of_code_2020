numbers = [int(n) for n in open('aoc2020/day_9/input.txt').read().splitlines()]

left, right = 0, 1
target = 32321523
sum = 0
sum += numbers[left]
while right < len(numbers) and left < len(numbers):
  if sum  == target:
    print(f'sum is found in {left},{right}')
    print(min(numbers[left:right+1]) + max(numbers[left:right+1]))
    break
  elif sum < target:
    sum += numbers[right]
    right += 1
  else:
    sum -= numbers[left]
    left += 1
  