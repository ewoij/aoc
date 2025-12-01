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

text = text.strip()
lines = text.split('\n')
lines = [(1 if v[0] == 'R' else -1) * int(v[1:]) for v in lines]

counter = 0
c = 50
for v in lines:
    c = (c + v) % 100
    if c == 0:
        counter += 1

print(counter)
