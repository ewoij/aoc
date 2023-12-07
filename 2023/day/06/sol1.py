#!/usr/bin/python3


def main():
    with open("2023/day/06/input") as f:
        lines = list(f)

    times = list(map(int, lines[0].split(':')[1].split()))
    distances = list(map(int, lines[1].split(':')[1].split()))

    nbeats = [0] * len(times)

    for i in range(len(times)):
        for j in range(times[i]+1):
            if (times[i]-j) * j > distances[i]:
                nbeats[i] += 1

    mul = 1
    for v in nbeats:
        mul *= v

    print(mul)



if __name__ == "__main__":
    main()
