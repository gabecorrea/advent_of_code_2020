from itertools import combinations

adapter_charges = [int(charge) for charge in open('aoc2020/day_10/input3.txt').read().splitlines()]
adapter_charges.sort()
adapter_charges.insert(0,0)
#adapter_charges.append(adapter_charges[-1] + 3)
print(adapter_charges)
#print(len(list(combinations([4,5,6,7], 2))))

# also account for charge from device adapter
# set of foursomes
foursome_members = set()
foursome_count = 0
isolated_threesome_count = 0
for i in range(1,len(adapter_charges) - 2):
  i, ii, iii, iv = adapter_charges[i-1], adapter_charges[i], adapter_charges[i+1], adapter_charges[i+2]
  if ii == i+1 and ii == iii - 1 and iii == iv - 1:
    foursome_members.update([i,ii,iii,iv])
    foursome_count += 1
  else:
    if ii == i+1 and ii == iii - 1 or ii == iii -1 and iii == iv - 1:
      if len(foursome_members & set([i,ii,iii,iv])) == 0:
        isolated_threesome_count += 1
print(foursome_count)
print((foursome_count * 6) + isolated_threesome_count + 1)