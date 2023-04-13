input = list(map(list, open('2022/day/12/input')))
input = [line[:-1] for line in input]
print(input)

m, n = len(input), len(input[0])

from itertools import product

E = S = (0, 0)
for ny, nx in product(range(m), range(n)):
    if input[ny][nx] == 'S':
        S = (ny, nx)
    if input[ny][nx] == 'E':
        E = (ny, nx)

input[S[0]][S[1]] = 'a'
input[E[0]][E[1]] = 'z'

queue = [E]
visited = set([E])
i = 0

parent = dict()

while queue:
    i += 1
    for _ in range(len(queue)):
        y, x = queue.pop(0)
        if input[y][x] == 'a':
            queue = None
            break
        for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if not (0 <= ny < m and 0 <= nx < n):
                continue
            if (ny, nx) in visited:
                continue
            if ord(input[ny][nx]) - ord(input[y][x]) < -1:
                continue
            queue.append((ny, nx))
            visited.add((ny, nx))
            parent[(ny, nx)] = (y, x)

        # at most 1 up
        # not visited


path = []
c = (y, x)
while c:
    path.append(c)
    c = parent.get(c)

print('got a', len(path) - 1)
#path.reverse()
#for p in path:
#    print(*p)
