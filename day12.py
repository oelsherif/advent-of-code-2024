import time
from collections import defaultdict
from copy import deepcopy

with open("inputs/12.txt", "r") as File:
    grid = [['.'] + list(line[:-1]) + ['.'] for line in File]

n_cols = len(grid[0])
grid = [['.'] * n_cols] + grid + [['.'] * n_cols]
n_rows = len(grid)

deltas = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

def count_corners(region):
    map = [[0] * n_cols for _ in range(n_rows)]
    min_x = min(tile[0] for tile in region)
    max_x = max(tile[0] for tile in region)
    min_y = min(tile[1] for tile in region)
    max_y = max(tile[1] for tile in region)
    for (x, y) in region:
        map[y][x] = 1
    ans = 0
    for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
            NW, NE = map[y][x], map[y][x+1]
            SW, SE = map[y+1][x], map[y+1][x+1]
            if (n_ones := NW + NE + SW + SE)%2:
                ans += 1
            elif n_ones == 2 and NW == SE:
                ans += 2
    return ans

t1 = time.time()
ans_p1, ans_p2 = 0, 0
for Y, row in enumerate(grid):
    for X, char in enumerate(row):
        if char == '.':
            continue
        if ord(char) in range(ord('a'), ord('z')+1):
            continue
        area, perim_p1 = 0, 0
        check_now, check_next = [(X, Y)], []
        low_char = char.lower()
        grid[Y][X] = low_char
        region = [] #list of tiles in the region
        while (check_now):
            for (x, y) in check_now:
                area += 1
                region.append((x, y))
                for (dx, dy) in deltas:
                    new_x, new_y = x+dx, y+dy
                    new_char = grid[new_y][new_x]
                    if new_char == low_char:
                        continue
                    if new_char == char:
                        check_next.append((new_x, new_y))
                        grid[new_y][new_x] = low_char
                    else:
                        perim_p1 += 1
            check_now = check_next[:]
            check_next = []
        perim_p2 = count_corners(region)
        ans_p1 += area * perim_p1
        ans_p2 += area * perim_p2

t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t2 - t1:.2f}s")
