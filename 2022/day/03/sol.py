lines = open('2022/day/3/input').readlines()

pairs = []
for line in lines:
    line = line.strip()
    a = line[:len(line) // 2]
    b = line[len(line) // 2:]
    pairs.append((a, b))


def get_value(c):
    is_lower = ord('a') <= ord(c) <= ord('z')
    c = c.lower()
    value = ord(c) - ord('a')
    return value + (1 if is_lower else 27)

for a, b in pairs:
    common_types = set(a) & set(b)
    for type in common_types:
        print(get_value(type))
