lines = [(a, int(b)) for a, b in map(str.split, open('2022/day/9/input'))]

s = (0, 0)
rope = [s] * 11

inc_by_dir = {
    'L': (0, -1),
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
}

def move(dir: str, pos):
    return tuple(map(sum, zip(pos, inc_by_dir[dir])))


def print_rope(rope, char=None):
    rope = list(rope) + [(0, 0)]
    top_most = min(rope, key=lambda x: x[0])[0]
    left_most = min(rope, key=lambda x: x[1])[1]

    rope = list((y - top_most, x - left_most) for y, x in rope)

    for y in range(20):
        for x in range(20):
            if (y, x) in rope:
                index = rope.index((y, x))
                c = char or str(index)
                if len(c) > 1:
                    c = 'T'
                if index == len(rope) - 1:
                    c = 's'
                print(c, end='')
            else:
                print('.', end='')
        print()

all_pos = { s }


print_rope(rope)
print()

for dir, n in lines:
    for _ in range(n):
        rope[0] = move(dir, rope[0])
        for i in range(1, len(rope)):
            h, t = rope[i-1], rope[i]
            dy, dx = t[0] - h[0], t[1] - h[1]
            if abs(dy) == 2 or abs(dx) == 2:
                rope[i] = (h[0] + int(dy / 2), h[1] + int(dx / 2))
        all_pos.add(rope[-1])

        print()
        print_rope(rope)
        print()
        input()

print(len(all_pos))
print_rope(all_pos, char='#')
