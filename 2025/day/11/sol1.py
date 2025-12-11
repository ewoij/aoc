txt = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

txt = open('2025/day/11/input.txt').read()


G: dict[str, set[str]] = dict()

for line in txt.strip().split('\n'):
    G[line.split(':')[0]] = set(map(str.strip, line.split(':')[1].split()))

def visit(hist: list[str]):
    if hist[-1] == 'out': return [hist]
    return [p for n in G[hist[-1]] if n not in hist for p in visit(hist + [n])]

print(len(visit(['you'])))
