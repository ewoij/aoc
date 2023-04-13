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

cycles = cpu(ops)

for _ in range(6):
    for i in range(40):
        _, x = next(cycles)
        print('#' if i in {x-1, x, x+1} else '.', end="")
    print()

###...##..###..#..#.###..####..##..###..
#..#.#..#.#..#.#..#.#..#.#....#..#.#..#.
#..#.#....#..#.####.###..###..#..#.###..
###..#.##.###..#..#.#..#.#....####.#..#.
#....#..#.#....#..#.#..#.#....#..#.#..#.
#.....###.#....#..#.###..####.#..#.###..

# PGPHBEAB
