#!/usr/bin/python3


def main():
    with open("2023/day/05/input") as f:
        groups = f.read().split("\n\n")

    seeds = list(map(int, groups[0].split(":")[1].split()))

    groups = [
        [list(map(int, line.split())) for line in g.split("\n")[1:] if line]
        for g in groups[1:]
    ]

    intervals = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
    intervals = merge_intervals(intervals)

    for g in groups:
        intervals = split_intervals(intervals, g)
        intervals = merge_intervals(intervals)
    print(intervals[0][0])
    

def split_intervals(intervals, map_):
    results = []
    while intervals:
        l1, r1 = intervals.pop()
        splitted = False
        for target, source, range_ in map_:
            l2, r2 = source, source + range_ - 1
            if l2 <= r1 and r2 >= l1:
                splitted = True
                l3, r3 = max(l1, l2), min(r1, r2)
                results.append((l3-l2+target, l3-l2+target+r3-l3))
                if l1 < l3:
                    intervals.append((l1,l3-1))
                if r3 < r1:
                    intervals.append((r3+1,r1))
                break
        if not splitted:
            results.append((l1, r1))
    return results


def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda v: v[0])
    results = [intervals[0]]
    for l2, r2 in intervals[1:]:
        l1, r1 = results[-1]
        if l2 <= r1:
            results[-1] = (l1, max(r1, r2))
        else:
            results.append((l2, r2))
    return results
    

if __name__ == "__main__":
    main()
