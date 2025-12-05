from functools import cache

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


def stuff(arr: list[int]):
    @cache
    def toto(start, items):
        if items == 0:
            return []
        if start > len(arr)-1:
            return []
        if items > len(arr):
            return []
        a = [arr[start]] + toto(start+1, items-1)
        b = toto(start+1, items)
        if to_int(a) > to_int(b):
            return a
        else:
            return b
    return toto(0, 12)

def to_int(arr: list[int]):
    res = 0
    for i, v in enumerate(reversed(arr)):
        res += v * 10 ** i
    return res


lines = [list(map(int, v)) for v in txt.strip().split('\n')]

print(lines)

res = 0
for line in lines:
    v = to_int(stuff(line))
    res += v
    print(v)

print(res)
