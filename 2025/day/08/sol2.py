from functools import reduce
from operator import mul

txt = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

txt = open('2025/day/08/input.txt').read()
nodes = [tuple(map(int, l.split(','))) for l in txt.strip().split('\n')]

def eucl(a, b):
    return sum((c2 - c1)**2 for c1, c2 in zip(a,b)) ** 0.5

distances = [(nodes[i], nodes[j], eucl(nodes[i], nodes[j])) for i in range(len(nodes)) for j in range(i+1, len(nodes))]
distances = sorted(distances, key=lambda v: v[-1])

groups = []

for a, b, _ in distances:
    ga = gb = -1
    for i in range(len(groups)):
        if a in groups[i]:
            ga = i
        if b in groups[i]:
            gb = i
    if ga == gb == -1:
        groups.append({a, b})
    elif ga == -1:
        groups[gb].add(a)
    elif gb == -1:
        groups[ga].add(b)
    elif ga == gb:
        pass
    else:
        groups[ga].update(groups[gb])
        groups.pop(gb)

    if len(groups) == 1 and len(groups[0]) == len(nodes):
        print(a[0] * b[0])
        break
