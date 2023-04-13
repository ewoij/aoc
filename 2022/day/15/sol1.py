import re


data = []
for line in open('2022/day/15/input'):
    pos = re.match(r"Sensor at x=(.*?), y=(.*?): closest beacon is at x=(.*?), y=(.*?)\n", line).groups()
    pos = list(map(eval, pos))
    data.append((tuple(pos[:2]), tuple(pos[2:])))

print(data)

row = 2_000_000

# calculer les intervals sur la ligne pour chaque sensor
intervals = []
for s, b in data:
    d = abs(s[0] - b[0]) + abs(s[1] - b[1])
    rd = abs(s[1] - row)
    if rd > d:
        continue
    # start end
    start, end = s[0] - (d - rd), s[0] + (d - rd)
    intervals.append((start, end))

xs = set()
for s, e in intervals:
    for x in range(s, e+1):
        xs.add(x)

# remove beacon in the set
for _, b in data:
    if b[1] == row and b[0] in xs:
        xs.remove(b[0])

# print(sorted(xs))
print(len(xs))
