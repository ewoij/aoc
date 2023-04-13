lines = open('2022/day/8/input').read().split('\n')[:-1]

grid = [list(map(int, line)) for line in lines]
m, n = len(grid), len(grid[0])

is_visible = [[False] * n for _ in range(m)]

for y in range(m):
    max_height = -1
    for x in range(n):
        is_visible[y][x] = is_visible[y][x] or grid[y][x] > max_height
        max_height = max(max_height, grid[y][x])

    max_height = -1
    for x in range(n-1, -1, -1):
        is_visible[y][x] = is_visible[y][x] or grid[y][x] > max_height
        max_height = max(max_height, grid[y][x])

for x in range(n):
    max_height = -1
    for y in range(m):
        is_visible[y][x] = is_visible[y][x] or grid[y][x] > max_height
        max_height = max(max_height, grid[y][x])

    max_height = -1
    for y in range(m-1, -1, -1):
        is_visible[y][x] = is_visible[y][x] or grid[y][x] > max_height
        max_height = max(max_height, grid[y][x])

print(sum(is_visible[y][x] for y in range(m) for x in range(n)))

# 1695
