
lines = open('2022/day/4/input').readlines()

pairs = []
for line in lines:
    a, b, c, d = list(map(int, line.split()))
    pairs.append(((a, b), (c, d)))

def contains(a, b):
    a_s, a_e = a
    b_s, b_e = b
    return a_s <= b_s and a_e >= b_e

def overlaps(a, b):
    a_s, a_e = a
    b_s, b_e = b
    return (
        (a_s <= b_s <= a_e) or 
        (a_s <= b_e <= a_e)
    )

for a, b in pairs:
    print(overlaps(a, b) or overlaps(b, a))
