import numpy as np
from functools import reduce
from operator import mul

from PIL import Image

def binary_to_green_image(arr):
    """
    arr: 2D numpy array with values 0 or 1
    output: PIL image where 0 = black, 1 = green
    """
    # convert binary to RGB channels
    # shape -> (H, W, 3)
    rgb = np.zeros((*arr.shape, 3), dtype=np.uint8)

    # green channel = 255 when arr == 1
    rgb[arr == 1] = [0, 255, 0]
    rgb[arr == 2] = [255, 0, 0]

    return Image.fromarray(rgb)

txt = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

txt = open('2025/day/09/input.txt').read()
tiles = [tuple(map(int, l.split(','))) for l in txt.strip().split('\n')]

def area(a, b):
    return reduce(mul, [abs(a-b)+1 for a, b in zip(a,b)])

tiles = np.array(tiles)
tiles_original = tiles.copy()

tiles = np.concatenate([tiles[:, [1]], tiles[:, [0]]], axis=1)
tiles = (tiles / 200).astype(int)

tiles[:, 0] = tiles[:, 0] - tiles[:, 0].min()
tiles[:, 1] = tiles[:, 1] - tiles[:, 1].min()

h = tiles[:, 0].max()+1
w = tiles[:, 1].max()+1

M = np.zeros((h, w), dtype=int)

for i in range(tiles.shape[0]):
    a = tiles[i, :]
    b = tiles[(i+1) % tiles.shape[0], :]
    r0, r1 = sorted([a[0], b[0]])
    c0, c1 = sorted([a[1], b[1]])
    M[r0:r1+1, c0:c1+1] = 1

# color
stack = [(M.shape[0] // 3, M.shape[1] // 2)]
while stack:
    r, c = stack.pop()
    M[r, c] = 1
    for r_ in range(r-1, r+1+1):
        for c_ in range(c-1, c+1+1):
            if M[r_, c_] == 0:
                stack.append((r_, c_))


# stuff
max_ = 0
max_pair = None

for i in range(tiles.shape[0]):
    print(i)
    for j in range(i+1, tiles.shape[0]):
        a = tiles[i, :]
        b = tiles[j, :]
        r0, r1 = sorted([a[0], b[0]])
        c0, c1 = sorted([a[1], b[1]])
        if list(np.unique(M[r0:r1+1, c0:c1+1])) == [1]:
            area_ = area(a, b)
            if area_ > max_:
                max_ = area_
                max_pair = (i, j)

a, b = max_pair
print(area(tiles_original[a, :], tiles_original[b, :]))

a, b = tiles[a, :], tiles[b, :]

r0, r1 = sorted([a[0], b[0]])
c0, c1 = sorted([a[1], b[1]])
M[r0:r1+1, c0:c1+1] = 2

binary_to_green_image(M).save('test.png')
