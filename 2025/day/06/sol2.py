import re
from functools import reduce
from operator import add, mul

txt = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


txt = open('2025/day/06/input.txt').read()


lines = [list(l) for l in txt.split('\n')]
lines = lines[:-1]

lines = '#'.join([''.join([lines[y][x] for y in range(len(lines))]) for x in reversed(range(len(lines[0])))])

exprs = re.split('# +#', lines)

r = 0
for expr in exprs:
    op = add if '+' in expr else mul
    expr = expr.replace('+', '')
    expr = expr.replace('*', '')
    expr = expr.split('#')
    expr = list(map(int, expr))
    r += reduce(op, expr)

print(r)
