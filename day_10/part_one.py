adapter_charges = [int(charge) for charge in open('aoc2020/day_10/input.txt').read().splitlines()]
adapter_charges.sort()
#print(len(adapter_charges))
differences = []
for index in range(len(adapter_charges) - 1):
  differences.append(adapter_charges[index+1] - adapter_charges[index])

# also account for charge from initial charger and device adapter
print(1+differences.count(1))
print(differences.count(2))
print((1 + differences.count(1)) * (differences.count(3) + 1))