group_answers = [set(answer.replace('\n', '')) for answer in open('aoc2020/day_6/input.txt').read().split('\n\n')]
print(sum([len(answer_set) for answer_set in group_answers]))
