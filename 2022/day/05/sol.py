stacks = [list(line[:-1]) for line in open("2022/day/5/input3_state")]
moves = [list(map(int, line.split())) for line in open("2022/day/5/input3_moves")]

for n, a, b in moves:
    a, b = a-1, b-1

    print('/--')
    for s in stacks:
        print(s)
    print('--/')

    print(n, a, b)

    stacks[b] = stacks[b] + stacks[a][-n:][-1::-1]
    stacks[a] = stacks[a][:-n]

    print('/--')
    for s in stacks:
        print(s)
    print('--/')

    input()

    print()
    print()


# CNSZFDVLJ
# QNDWLMGNS


