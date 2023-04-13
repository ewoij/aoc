lines = open('2022/day/8/input').read().split('\n')[:-1]

grid = [list(map(int, line)) for line in lines]
m, n = len(grid), len(grid[0])

result = 0

for y in range(m):
    for x in range(n):
        print((y * n + x) / (m * n))
        result_ = []

        x1, y1 = x, y
        for x1 in range(x - 1, -1, -1):
            if grid[y1][x1] >= grid[y][x]:
                break
        result_.append(abs(x1 - x + y1 - y))

        x1, y1 = x, y
        for x1 in range(x + 1, n):
            if grid[y1][x1] >= grid[y][x]:
                break
        result_.append(abs(x1 - x + y1 - y))

        x1, y1 = x, y
        for y1 in range(y - 1, -1, -1):
            if grid[y1][x1] >= grid[y][x]:
                break
        result_.append(abs(x1 - x + y1 - y))

        x1, y1 = x, y
        for y1 in range(y + 1, m):
            if grid[y1][x1] >= grid[y][x]:
                break
        result_.append(abs(x1 - x + y1 - y))

        result_mul = result_[0]
        for i in range(1, len(result_)):
            result_mul *= result_[i]

        result = max(result, result_mul)

print(result)


