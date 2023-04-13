lines = open('2022/day/3/input').readlines()

lines = [line.strip() for line in lines]

def get_value(c):
    is_lower = ord('a') <= ord(c) <= ord('z')
    c = c.lower()
    value = ord(c) - ord('a')
    return value + (1 if is_lower else 27)

res = 0
for i in range(0, len(lines), 3):
    sets = list(map(set, lines[i:i+3]))
    common = sets[0]
    for i in range(1, len(sets)):
        common = common & sets[i]
    res += get_value(next(iter(common)))

print(res)
