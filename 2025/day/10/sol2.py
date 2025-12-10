from dataclasses import dataclass
import pulp as pl

txt = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

@dataclass
class Machine:
    buttons: list[list[int]]
    target: list[int]


txt = open('2025/day/10/input.txt').read()

machines = []
for line in txt.strip().split('\n'):
    parts = line.split()
    machines.append(Machine(
        buttons=[list(map(int, p[1:-1].split(','))) for p in parts[1:-1]],
        target=list(map(int, parts[-1][1:-1].split(',')))
    ))


def solve(machine: Machine):
    prob = pl.LpProblem('toto', pl.LpMinimize)

    vars = [pl.LpVariable(str(j), lowBound=0, cat=pl.LpInteger) for j in range(len(machine.buttons))]

    for i in range(len(machine.target)):
        vars_ = [vars[j] for j, v in enumerate(machine.buttons) if i in v]
        prob += sum(vars_) == machine.target[i], f'sum {i}'

    prob += sum(vars), 'minimize sum'

    prob.solve()

    return [v.varValue for v in vars]

res = 0
for m in machines:
    r = sum(solve(m))
    print(r)
    res += r

print(res)
