def bus_arrival_times(start, bus_id):
  count = (start // bus_id) + 1
  while True:
    yield (bus_id, count * bus_id)
    count += 1

file = open('aoc2020/day_13/input.txt')
starting_timestamp = int(next(file))
arrivals = [bus_arrival_times(starting_timestamp, int(id)) for id in next(file).split(',') if id != 'x']

next_arrivals = [next(arrival) for arrival in arrivals]
next_arrivals.sort(key = lambda a: a[1])
first = next_arrivals[0]
print(first[0] * (first[1] - starting_timestamp))
