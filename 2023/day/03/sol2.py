#!/usr/bin/python3

def main():
    with open('2023/day/03/input') as f:
        lines  = [line.rstrip() for line in f]

    numbers_by_stars = {}
    for y in range(len(lines)):
        x = 0
        while x < len(lines[y]):
            begin_x = x
            while x < len(lines[y]) and lines[y][x].isdigit():
                x += 1
            end_x = x

            if begin_x < end_x:
                for star_pos in find_all_stars_around_word(lines, y, begin_x, end_x - begin_x):
                    numbers_by_stars.setdefault(star_pos, []).append(int(lines[y][begin_x:end_x]))

            while x < len(lines[y]) and not lines[y][x].isdigit():
                x += 1

    gears = { pos: numbers for pos, numbers in numbers_by_stars.items() if len(numbers) == 2}

    ratios = [ a * b for a, b in gears.values()]

    print(sum(ratios))


def find_all_stars_around_word(lines, y, x, len_):
    for y_ in range(max(0, y-1), min(len(lines), y+1+1)):
        for x_ in range(max(0, x-1), min(len(lines[y_]), x+len_+1)):
            if lines[y_][x_] == '*':
                yield (y_, x_)


if __name__ == "__main__":
    main()
