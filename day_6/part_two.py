group_answers = [sorted(answer.split('\n'), key=lambda x: len(x)) for answer in open('aoc2020/day_6/input.txt').read().split('\n\n')]

all_answered = 0
for group in group_answers:
  if len(group) == 1:
    all_answered += len(group[0])
    continue
  target_count = len(group) - 1
  test_answers = group.pop(0)

  for char in list(test_answers):
    occurrences = sum(char in answers for answers in group)
    if occurrences == target_count:
      all_answered += 1
  
print(all_answered)
