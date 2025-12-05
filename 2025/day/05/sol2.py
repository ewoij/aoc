txt = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


txt = open('2025/day/05/input.txt').read()


txt = txt.strip()
ranges, ingredients = txt.split('\n\n')

ranges = [tuple(map(int,v.split('-'))) for v in ranges.split('\n')]

# merge intervals
ranges = sorted(ranges)

res = [ranges[0]]
for v in ranges[1:]:
    if res[-1][1] >= v[0]:
        res[-1] = (res[-1][0], max(res[-1][1], v[1]))
    else:
        res += [v]

ranges = res

# compute ingredients
print(sum(e - s + 1 for s, e in ranges))
