elves = set()

for y, line in enumerate(open('2022/day/23/input')):
    for x, v in enumerate(line):
        if v == '#':
            elves.add((x, y))


def get_next_pos_N(pos, elves):
    x, y = pos
    for dx in range(-1, 1+1):
        p2 = (x+dx,y-1)
        if p2 in elves:
            return None
    return (x, y-1)


def get_next_pos_S(pos, elves):
    x, y = pos
    for dx in range(-1, 1+1):
        p2 = (x+dx,y+1)
        if p2 in elves:
            return None
    return (x, y+1)


def get_next_pos_W(pos, elves):
    x, y = pos
    for dy in range(-1, 1+1):
        p2 = (x-1,y+dy)
        if p2 in elves:
            return None
    return (x-1,y)


def get_next_pos_E(pos, elves):
    x, y = pos
    for dy in range(-1, 1+1):
        p2 = (x+1,y+dy)
        if p2 in elves:
            return None
    return (x+1,y)


next_pos_rules = [
    get_next_pos_N,
    get_next_pos_S,
    get_next_pos_W,
    get_next_pos_E,
]


def print_elves():
    for y in range(15):
        for x in range(15):
            print('.' if (x, y) not in elves else '#', end='')
        print()



for i in range(1000):
    new_dests = dict()

    for elve in elves:
        new_des = elve
        if sum(1 for dx in range(-1, 1+1) for dy in range(-1,1+1) if (elve[0]+dx, elve[1]+dy) in elves) == 1:
            pass
        else:
            for get_next_pos in next_pos_rules:
                new_des_tmp = get_next_pos(elve, elves)
                if new_des_tmp:
                    new_des = new_des_tmp
                    break
        new_dests.setdefault(new_des, []).append(elve)

    new_elves = set()
    for new_dest, elves_ in new_dests.items():
        if len(elves_) == 1:
            new_elves.add(new_dest)
        else:
            new_elves.update(elves_)

    next_pos_rules.append(next_pos_rules.pop(0))

    if elves == new_elves:
        print(i+1)
        break
    else:
        elves = new_elves
