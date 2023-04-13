import re

blueprints = []
for line in open('2022/day/19/input_test'):
    arr =  list(map(int, re.findall(r'\d+', line)))
    blueprints.append({
        'ore': { 'ore': arr[1] },
        'clay': { 'ore': arr[2] },
        'obsidian': { 'ore': arr[3], 'clay': arr[4] },
        'geode': { 'ore': arr[5], 'obsidian': arr[6] },
    })


def poss_new_robots(blueprint, resources, curr=0, order=['ore', 'clay', 'obsidian', 'geode']):
    if curr == len(order):
        yield dict()
        return
    t = order[curr] # robot type
    n = 0 # number of robots
    while resources[t] - n * blueprint[t] >= 0:
        for poss in poss_new_robots(blueprint, resources | { t: resources[t] - n * blueprint[t] }, curr+1):
            poss[t] = n
            yield poss
        n += 1


blueprint = blueprints[0]
context = dict(robots=dict(ore=1), resources={})

for poss in poss_new_robots(blueprints[0], dict(ore=4)):
    print(poss)
