#!/usr/bin/python3

def main():
    with open('2023/day/04/input') as f:
        lines  = [line.rstrip() for line in f]

    result = 0
    for line in lines:
        winners, actual = [{int(v) for v in v.split()} for v in line.split(':')[1].split('|')]
        len_ = len(winners & actual)
        result += len_ and 2 ** (len_ - 1)

    print(result)


if __name__ == "__main__":
    main()
