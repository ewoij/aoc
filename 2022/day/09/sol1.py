lines = [(a, int(b)) for a, b in map(str.split, open('2022/day/9/input'))]

h = t = s = (0, 0)

inc_by_dir = {
    'L': (0, -1),
    'U': (1, 0),
    'R': (0, 1),
    'D': (-1, 0),
}

opp_by_dir = {
    'L': 'R',
    'U': 'D',
    'R': 'L',
    'D': 'U',
}

def move(dir: str, pos):
    return tuple(map(sum, zip(pos, inc_by_dir[dir])))

all_pos = { t }

for dir, n in lines:
    for _ in range(n):
        h = move(dir, h)
        if max(abs(h[0] - t[0]), abs(h[1] - t[1])) > 1:
            t = move(opp_by_dir[dir], h)
            all_pos.add(t)

print(len(all_pos))

# 6209
