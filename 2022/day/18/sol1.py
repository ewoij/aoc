blocks = {tuple(map(int, l.split(','))) for l in open('2022/day/18/input')}

def get_adj_neighs(pos):
    for dim in range(len(pos)):
        for diff in [-1, 1]:
            neigh = list(pos)
            neigh[dim] += diff
            yield tuple(neigh)

total = 0
for block in blocks:
    busy_sides = sum(n in blocks for n in get_adj_neighs(block))
    free_sides = 6 - busy_sides
    total += free_sides

print(total)
