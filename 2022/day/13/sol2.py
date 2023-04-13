from functools import cmp_to_key

pairs = open('2022/day/13/input').read()[:-1].split('\n\n')
pairs = [list(map(eval, p.split('\n'))) for p in pairs]

def in_order(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            r = in_order(a[i], b[i])
            if r != 0:
                return r
        return len(a) - len(b)
    elif isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, int):
        return in_order([a], b)
    else:
        return in_order(a, [b])


packets = [p for p in pairs for p in p]

packets.sort(key=cmp_to_key(in_order))

for p in packets:
    print(p)

p1 = packets.index([[2]]) + 1
p2 = packets.index([[6]]) + 1

print(p1 * p2)
