from functools import reduce
from operator import mul

txt = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

txt = open('2025/day/09/input.txt').read()
tiles = [tuple(map(int, l.split(','))) for l in txt.strip().split('\n')]

def area(a, b):
    return reduce(mul, [abs(a-b)+1 for a, b in zip(a,b)])

areas = [(i, j, area(tiles[i], tiles[j])) for i in range(len(tiles)) for j in range(i+1, len(tiles))]
areas = sorted(areas, key=lambda v: -v[-1])
print(tiles[areas[0][0]])
print(tiles[areas[0][1]])
print(areas[0][2])
