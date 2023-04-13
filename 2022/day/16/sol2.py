import re
import functools

graph = dict()

rate_by_valve = dict()

for line in open('2022/day/16/input').read()[:-1].split('\n'):
    groups = re.match(r'Valve (.*?) has flow rate=(.*?); tunnels? leads? to valves? (.*)', line).groups()
    graph.setdefault(groups[0], set()).update(set(groups[2].split(', ')))
    rate_by_valve[groups[0]] = int(groups[1])


@functools.cache
def dfs(node_c, node_e, mins, opened):
    if mins < 2: return 0
    can_open_c = node_c not in opened and rate_by_valve[node_c] > 0
    r1 = 0
    if can_open:
        new_opened = tuple(sorted(opened + (node,)))
        r1 = max(rate_by_valve[node] * (mins -1) + dfs(neigh, mins - 2, new_opened) for neigh in graph.get(node, []))

    r2 = max(dfs(neigh, mins - 1, opened) for neigh in graph.get(node, []))
    return max(r1, r2)

    
@functools.cache
def dfs(node_c, node_c_ing, node_e, node_e_ing, mins, opened):
    if mins < 2: return 0
    if node_c_ing:
        rate_by_valve[node] * (mins -1)

    can_open_c = node_c not in opened and rate_by_valve[node_c] > 0
    r1 = 0
    if can_open:
        new_opened = tuple(sorted(opened + (node,)))
        r1 = max(rate_by_valve[node] * (mins -1) + dfs(neigh, mins - 2, new_opened) for neigh in graph.get(node, []))

    r2 = max(dfs(neigh, mins - 1, opened) for neigh in graph.get(node, []))
    return max(r1, r2)

    
print(dfs('AA', 30, tuple()))
