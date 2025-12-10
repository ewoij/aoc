from functools import cache
from dataclasses import dataclass

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


def toto(machine: Machine):
    buttons = machine.buttons
    buttons = sorted(buttons, key=lambda v: -len(v))
    target = tuple(machine.target)

    def next_(target, button):
        target = list(target)
        for i in button:
            target[i] -= 1
        return tuple(target)

    def find_max(target, button):
        assert all(v >= 0 for v in target), 'invalid state'
        c = 0
        while not any(v < 0 for v in target):
            target = next_(target, button)
            c += 1
        return c - 1

    def backtrack(idx, target):
        if idx >= len(buttons): 
            if all(v == 0 for v in target):
                return []
            else:
                return None
        max_ = find_max(target, buttons[idx])
        for i in reversed(range(max_+1)):
            n_target = target
            for _ in range(i):
                n_target = next_(n_target, buttons[idx])
            res = backtrack(idx+1, n_target)
            if res is not None: return [i] + res
        return None

    return backtrack(0, target)


toto(machines[4])

# res = 0
# for m in machines:
#     r = toto(m)
#     print(sum(r), r)
#     res += sum(r)
# 
# print(res)
