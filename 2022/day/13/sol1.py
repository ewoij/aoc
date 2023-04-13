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


print(sum(i + 1 for i, (a, b) in enumerate(pairs) if in_order(a, b) < 0))
