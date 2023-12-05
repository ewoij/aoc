#!/usr/bin/python3


# Too slow
def main():
    with open("2023/day/05/input") as f:
        groups = f.read().split("\n\n")

    seeds = list(map(int, groups[0].split(":")[1].split()))

    groups = [
        [list(map(int, line.split())) for line in g.split("\n")[1:] if line]
        for g in groups[1:]
    ]

    min_location = float('inf')
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i]+seeds[i+1]):
            for g in groups:
                for target, source, range_ in g:
                    if source <= seed <= (source + range_):
                        seed = target + seed - source
                        break
            min_location = min(min_location, seed)

    print(min_location)


if __name__ == "__main__":
    main()
