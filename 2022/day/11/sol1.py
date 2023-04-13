monkeys = open('2022/day/11/input').read()[:-1].split('\n\n')
monkeys = [m.split('\n') for m in monkeys]
for i in range(len(monkeys)):
    monkeys[i] = monkeys[i][:2] + list(map(int, monkeys[i][2:]))

items_by_monkey = { i: list(map(int, m[0].split(', '))) for i, m in enumerate(monkeys) }

inspected_by_monkey = {}

for turn in range(20):
    for mi, m in enumerate(monkeys):
        inspected_by_monkey[mi] = inspected_by_monkey.get(mi, 0) + len(items_by_monkey[mi])
        while items_by_monkey[mi]:
            items = items_by_monkey[mi]
            old = items.pop(0)
            new = eval(m[1])
            new = new // 3
            next_monkey = int(m[3] if new % m[2] == 0 else m[4])
            items_by_monkey[next_monkey].append(new)

for pair in items_by_monkey.items():
    print(*pair)
print()
for pair in inspected_by_monkey.items():
    print(*pair)
print()
(_, a), (_, b) = sorted(inspected_by_monkey.items(), key=lambda v: v[1])[-2:]
print(a * b)

