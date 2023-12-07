#!/usr/bin/python3
from math import sqrt, floor, ceil


def main():
    with open("2023/day/06/input") as f:
        lines = list(f)

    t, d = [int(line.split(':')[1].replace(' ', '')) for line in lines]

    left = (-t + sqrt(t**2 - 4*d)) / -2
    right = (-t - sqrt(t**2 - 4*d)) / -2
    
    print(floor(right) - ceil(left) + 1)
    

if __name__ == "__main__":
    main()
