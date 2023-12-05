#!/usr/bin/python3


def main():
    with open("2023/day/05/input") as f:
        groups = f.read().split("\n\n")

    seeds = list(map(int, groups[0].split(":")[1].split()))

    groups = [
        [list(map(int, line.split())) for line in g.split("\n")[1:] if line]
        for g in groups[1:]
    ]

    locations = []
    for seed in seeds:
        v = seed
        for g in groups:
            for target, source, range_ in g:
                if source <= v <= (source + range_):
                    v = target + v - source
                    break
        locations.append(v)

    print(min(locations))


if __name__ == "__main__":
    main()
