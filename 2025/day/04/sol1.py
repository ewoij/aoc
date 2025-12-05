from collections import Counter 
txt = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


txt = open('2025/day/04/input.txt').read()


lines = txt.strip().split('\n')


def get_adj(x, y):
    coords = {(i, j) for i in range(x-1, x+1+1) for j in range(y-1, y+1+1) if i >= 0 and j >= 0}
    coords -= {(x, y)}
    res = []
    for i, j in coords:
        try:
            res.append(lines[i][j])
        except:
            res.append('.')
    return res


res = 0
for x in range(len(lines)):
    for y in range(len(lines[x])):
        print(x, y, Counter(get_adj(x, y))['@'])
        res += lines[x][y] == '@' and Counter(get_adj(x, y))['@'] < 4

print(res)
