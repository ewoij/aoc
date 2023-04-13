import re
from collections import Counter


data = []
for line in open('2022/day/15/input'):
    pos = re.match(r"Sensor at x=(.*?), y=(.*?): closest beacon is at x=(.*?), y=(.*?)\n", line).groups()
    pos = list(map(eval, pos))
    data.append((tuple(pos[:2]), tuple(pos[2:])))


def merge_intervals(intervals):
    if not intervals: return intervals
    intervals.sort()
    results = intervals[0:1]
    for interval in intervals[1:]:
        if results[-1][1] >= interval[0]:
            results[-1] = (results[-1][0], max(results[-1][1], interval[1]))
        else:
            results.append(interval)
    return results


for row in range(3_205_729, 4_000_000+1):
    intervals = []

    for s, b in data:
        d = abs(s[0] - b[0]) + abs(s[1] - b[1])
        rd = abs(s[1] - row)
        if rd > d:
            continue
        # start end
        start, end = s[0] - (d - rd), s[0] + (d - rd)
        intervals.append((start, end))

    intervals = merge_intervals(intervals)
    if len(intervals) > 1:
        break # 3_205_729

print(intervals) # [(-585465, 3283508), (3283510, 4284240)]
y = 3_205_729
x = 3283509

print(x * 4000000 + y)
