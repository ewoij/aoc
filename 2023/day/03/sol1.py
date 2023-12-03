#!/usr/bin/python3

def main():
    with open('2023/day/03/input') as f:
        lines  = [line.rstrip() for line in f]

    numbers = []
    for y in range(len(lines)):
        x = 0
        while x < len(lines[y]):
            begin_x = x
            while x < len(lines[y]) and lines[y][x].isdigit():
                x += 1
            end_x = x

            if begin_x < end_x and is_connected_to_symbol(lines, y, begin_x, end_x - begin_x):
                numbers.append(int(lines[y][begin_x:end_x]))

            while x < len(lines[y]) and not lines[y][x].isdigit():
                x += 1

    print(sum(numbers))


def is_connected_to_symbol(lines, y, x, len_):
    for y_ in range(max(0, y-1), min(len(lines), y+1+1)):
        for x_ in range(max(0, x-1), min(len(lines[y_]), x+len_+1)):
            c = lines[y_][x_]
            is_symbol = not c.isdigit() and c != '.'
            if is_symbol:
                return True
    return False


if __name__ == "__main__":
    main()
