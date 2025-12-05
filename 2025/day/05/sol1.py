txt = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


txt = open('2025/day/05/input.txt').read()


txt = txt.strip()
ranges, ingredients = txt.split('\n\n')

ranges = [list(map(int,v.split('-'))) for v in ranges.split('\n')]
ingredients = list(map(int, ingredients.split('\n')))

res = 0
for ing in ingredients:
    for s, e in ranges:
        if s <= ing <= e:
            res += 1
            print(ing)
            break

print()
print(res)
