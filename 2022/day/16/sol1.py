import re
import functools

graph = dict()

rate_by_valve = dict()

for line in open('2022/day/16/input').read()[:-1].split('\n'):
    groups = re.match(r'Valve (.*?) has flow rate=(.*?); tunnels? leads? to valves? (.*)', line).groups()
    graph.setdefault(groups[0], set()).update(set(groups[2].split(', ')))
    rate_by_valve[groups[0]] = int(groups[1])


@functools.cache
def dfs(node, mins, opened):
    if mins < 2: return 0
    can_open = node not in opened and rate_by_valve[node] > 0
    r1 = 0
    if can_open:
        new_opened = tuple(sorted(opened + (node,)))
        r1 = max(rate_by_valve[node] * (mins -1) + dfs(neigh, mins - 2, new_opened) for neigh in graph.get(node, []))

    r2 = max(dfs(neigh, mins - 1, opened) for neigh in graph.get(node, []))
    return max(r1, r2)

    
print(dfs('AA', 30, tuple()))
