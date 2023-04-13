from operator import add, sub, mul, truediv

graph = dict()

for line in open('2022/day/21/input'):
    k, v = line.split(":")
    v = v.split()
    graph[k] = int(v[0]) if len(v) == 1 else v

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

def dfs(node):
    if isinstance(graph[node], int):
        return graph[node]
    else:
        a, op, b = graph[node]
        return ops[op](dfs(a), dfs(b))

print(dfs('root'))
