from functools import cache

txt = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


txt = open('2025/day/07/input.txt').read()


txt = txt.strip()
arr = [list(l) for l in txt.split('\n')]


@cache
def browse(i, j):
    if i == len(arr) - 1:
        return 1
    i += 1
    if arr[i][j] == '^':
        return browse(i, j-1) + browse(i, j+1)
    else:
        return browse(i, j)


def print_path(path):
    arr_ = [list(l) for l in arr]
    for i, j in path:
        arr_[i][j] = '|'
    for l in arr_:
        print(''.join(l))
    import time
    # time.sleep(0.1)
    print()


def browse2(i, j, path):
    if i == len(arr) - 1:
        print_path(path)
        return 1
    i += 1
    if arr[i][j] == '^':
        return browse2(i, j-1, path + [(i, j-1)]) + browse2(i, j+1, path + [(i, j-1)])
    else:
        return browse2(i, j, path + [(i, j)])


print(browse(1, 70))
# print(browse2(1, 70, [(1, 7)]))
