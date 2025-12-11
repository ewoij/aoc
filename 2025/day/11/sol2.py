txt = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

from functools import cache, reduce
from itertools import permutations
from operator import mul

txt = open('2025/day/11/input.txt').read()

G: dict[str, set[str]] = dict()

for line in txt.strip().split('\n'):
    G[line.split(':')[0]] = set(map(str.strip, line.split(':')[1].split()))

@cache
def visit(curr: str, dest: str):
    if curr == dest: return 1
    return sum(visit(n, dest) for n in G.get(curr, set()))

s = 0
for r in [['svr'] + list(p) + ['out'] for p in permutations(['fft', 'dac'])]:
    s += reduce(mul, (visit(r[i], r[i+1]) for i in range(len(r)-1)))

print(s)
