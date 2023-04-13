paths = open('2022/day/14/input').read()[:-1].split('\n')

def gen(paths):
    for p in paths:
        p = p.split(' -> ')
        p = [list(map(int, p.split(','))) for p in p]
        for i in range(len(p)-1):
            yield p[i], p[i+1]

start = (500, 0)
min_x = max_x = 500
min_y = max_y = 0

for a, b in gen(paths):
    min_x = min(min_x, a[0], b[0])
    min_y = min(min_y, a[1], b[1])
    max_x = max(max_x, a[0], b[0])
    max_y = max(max_y, a[1], b[1])

min_x = 0
max_x = 700
max_y += 2

grid = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

for x in range(len(grid[-1])):
    grid[-1][x] = '#'

for a, b in gen(paths):
    for x in range(min(a[0], b[0]), max(a[0], b[0])+1):
        for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
            grid[y-min_y][x-min_x] = '#'

def print_grid(grid, m = None):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print('S' if m is not None and m[0] == x and m[1] == y else grid[y][x], end="")
        print()


def sand_flow():
    while True:
        x, y = start
        x, y = x - min_x, y - min_y

        while True:
            # print_grid(grid, (x, y))
            stuck = True
            for y2, x2 in [(y+1, x), (y+1, x-1), (y+1, x+1)]:
                if y2 >= len(grid):
                    print('y is out.')
                    return
                if not (0 <= x2 < len(grid[y2])):
                    print('x is out.')
                    return
                if grid[y2][x2] == '.':
                    stuck = False
                    y, x = y2, x2
                    break

            if stuck and (y, x) == (0, 500):
                grid[y][x] = 'o'
                print('stop')
                return
            if stuck:
                grid[y][x] = 'o'
                break

sand_flow()


count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'o':
            count += 1

print_grid(grid)
print(count)
