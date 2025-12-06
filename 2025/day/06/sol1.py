txt = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


txt = open('2025/day/06/input.txt').read()


txt = txt.strip()
lines = [l.split() for l in txt.split('\n')]

vals = lines[:-1]
ops = lines[-1]

vals = [list(map(int, l)) for l in vals]

res = 0

for x in range(len(vals[0])):
    vals_ = [vals[y][x] for y in range(len(vals))]
    op = ops[x]

    r = vals_[0]
    for v in vals_[1:]:
        if op == '*':
            r *= v
        else:
            r += v

    res += r
    print(r)


print(res)
