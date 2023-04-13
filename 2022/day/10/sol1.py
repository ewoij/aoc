def cpu(ops):
    i = x = 1

    for op in ops:
        if op is None:
            yield i, x; i += 1
        else:
            yield i, x; i += 1
            yield i, x; i += 1
            x += op

    yield i, x

ops = [int(items[1]) if len(items) == 2 else None for items in map(str.split, open('2022/day/10/input'))]
cycles = dict(cpu(ops))
print(sum(v * cycles[v] for v in [20, 60, 100, 140, 180, 220]))
