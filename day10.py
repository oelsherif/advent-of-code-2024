from collections import defaultdict
with open("inputs/10_test.txt", "r") as File:
    grid = [[-1] + [int(char) for char in line[:-1]] + [-1] for line in File]

n_cols = len(grid[0])
grid = [[-1] * n_cols] + grid + [[-1] * n_cols]

here = defaultdict(int)
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if num == 0:
            here[(x, y)] += 1

deltas = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

for next_num in range(1, 10):
    next = defaultdict(int)
