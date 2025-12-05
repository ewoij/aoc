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
lines = [list(l) for l in lines]


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


def toto():
    res = []
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            r = lines[x][y] == '@' and Counter(get_adj(x, y))['@'] < 4
            if r:
                res.append((x, y))
    return res


res = 0
while True:
    r = toto()
    print(len(r))
    res += len(r)

    for x, y in r:
        lines[x][y] = '.'

    if len(r) == 0:
        break

print(res)
