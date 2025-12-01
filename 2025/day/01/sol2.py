text = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

text = open('2025/day/01/input.txt').read()

text = text.strip()
lines = text.split('\n')
lines = [(1 if v[0] == 'R' else -1) * int(v[1:]) for v in lines]

counter = 0
c = 50
for v in lines:
    curr = c
    d, c = divmod(c + v, 100)
    d = abs(d)
    if v < 0:
        if c == 0:
            d += 1
        if curr == 0:
            d -= 1
    print(curr, v, c, d)
    counter += d

print()
print(counter)
