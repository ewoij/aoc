from itertools import cycle

seq = open('2022/day/17/input').read()[:-1]
rocks = [l.split('\n') for l in open('2022/day/17/rocks.txt').read()[:-1].split('\n\n')]

cave = []
cave_width = 7
rock_start_height = 3

cave.append(['#'] * (cave_width + 2))

def new_level():
    return ['#'] + ['.'] * cave_width + ['#']

def collide(cave, rock, x, y):
    for y2, rock_l in enumerate(rock):
        for x2, rock_v in enumerate(rock_l):
            if rock_v == '#' and cave[y - y2][x + x2] != '.':
                return True
    return False

def print_cave(cave):
    for l in cave[::-1]:
        print(''.join(l))

def print_cave2(cave, rock, x, y):
    cave2 = [[c for c in line] for line in cave]
    for y2, rock_l in enumerate(rock):
        for x2, rock_v in enumerate(rock_l):
            if rock_v == '#':
                cave2[y-y2][x+x2] = '@'
    for l in cave2[::-1]:
        print(''.join(l))

seq_iter = cycle(seq)

for rock_i, rock in enumerate(cycle(rocks)):
    if rock_i == 3000:
        break
    for _ in range(rock_start_height + len(rock)):
        cave.append(new_level())
    x, y = 3, len(cave) - 1
    for h_dir in seq_iter:
        h_dir = -1 if h_dir == '<' else 1
        if not collide(cave, rock, x + h_dir, y):
            x, y = x + h_dir, y
        if not collide(cave, rock, x, y - 1):
            x, y = x        , y - 1
        else:
            break
    for y2, rock_l in enumerate(rock):
        for x2, rock_v in enumerate(rock_l):
            if rock_v == '#':
                cave[y-y2][x+x2] = '#'
    while cave[-1] == new_level():
        cave.pop()

print(len(cave)-1)
