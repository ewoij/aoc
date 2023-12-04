#!/usr/bin/python3
from collections import Counter

def main():
    with open('2023/day/04/input') as f:
        lines  = [line.rstrip() for line in f]

    C = Counter()
    for i, line in enumerate(lines):
        C[i] += 1
        winners, actual = [{int(v) for v in v.split()} for v in line.split(':')[1].split('|')]
        len_ = len(winners & actual)
        for j in range(i+1, min(len(lines), i+1+len_)):
            C[j] += C[i]

    print(sum(C.values()))


if __name__ == "__main__":
    main()
