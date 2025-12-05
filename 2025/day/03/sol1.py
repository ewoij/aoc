txt = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


txt = open('2025/day/03/input.txt').read()

def largest(arr: list[int]):
    max_ = arr[0]
    res = 0
    for v in arr[1:]:
        r = max_ * 10 + v
        if r > res:
            res = r
        if v > max_:
            max_ = v
    return res


lines = [list(map(int, v)) for v in txt.strip().split('\n')]

print(lines)

for line in lines:
    print(largest(line))

print(sum(largest(line) for line in lines))
