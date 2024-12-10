from collections import defaultdict
with open("inputs/10.txt", "r") as File:
    grid = [[-1] + [int(char) for char in line[:-1]] + [-1] for line in File]

n_cols = len(grid[0])
grid = [[-1] * n_cols] + grid + [[-1] * n_cols]

deltas = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

here = defaultdict(set)
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if num == 9:
            here[(x, y)] |= {(x,y)}

for prev_height in range(8, -1, -1):
    prev = defaultdict(set)
    for (x, y), peaks in here.items():
        for dx, dy in deltas:
            new_x, new_y = x+dx, y+dy
            if grid[new_y][new_x] == prev_height:
                prev[(new_x, new_y)] |= peaks
    here = prev.copy()

ans_p1 = sum([len(peak_list) for peak_list in here.values()])
print(f"Part 1 answer: {ans_p1}")

here = defaultdict(int)
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if num == 0:
            here[(x, y)] += 1

for next_height in range(1, 10):
    next = defaultdict(int)
    for (x, y), count in here.items():
        for dx, dy in deltas:
            new_x, new_y = x+dx, y+dy
            if grid[new_y][new_x] == next_height:
                next[(new_x, new_y)] += count
    here = next.copy()

ans_p2 = sum(here.values())
print(f"Part 2 answer: {ans_p2}")
