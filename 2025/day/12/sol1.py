txt = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

txt = open('2025/day/12/input.txt').read()

txt = txt.strip().split('\n\n')

gift = [v.split(':\n')[-1] for v in txt[:-1]]
dim = [list(map(int, v.split(':')[0].split('x'))) for v in txt[-1].split('\n')]
gift_count = [list(map(int, v.split(':')[1].split())) for v in txt[-1].split('\n')]

s = 0
for i in range(len(dim)):
    r = False
    if dim[i][0] * dim[i][1] < sum(c * gift[j].count('#') for j, c in enumerate(gift_count[i])):
        r = False # for sure false
    elif dim[i][0] * dim[i][1] > sum(gift_count[i]) * 9:
        r = True # for sure true
    else:
        r = True # we don't know, assume true
    s += r
    print(r)

# lol

print(s)
