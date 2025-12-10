from dataclasses import dataclass

txt = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

@dataclass
class Machine:
    diag: tuple
    wiring: list[list[int]]


txt = open('2025/day/10/input.txt').read()

machines = []
for line in txt.strip().split('\n'):
    parts = line.split()
    diag = tuple(v == '#' for v in parts[0][1:-1])
    machines.append(Machine(diag=diag, wiring=[list(map(int, p[1:-1].split(','))) for p in parts[1:-1]]))


def count(machine: Machine):
    def next_state(state: tuple, wiring):
        return tuple(not v if i in wiring else v for i, v in enumerate(state))
    
    q = { (False,) * len(machine.diag) }
    c = 0
    while machine.diag not in q:
        q = { next_state(state, set(machine.wiring[i])) for state in q for i in range(len(machine.wiring))}
        c += 1

    return c
        
print(sum(count(machines[i]) for i in range(len(machines))))
