from copy import deepcopy
import time
from collections import defaultdict
with open("inputs/20.txt", "r") as File:
    lines = File.readlines()

orig_grid = [list(line[:-1]) for line in lines]
grid = deepcopy(orig_grid)
n_rows, n_cols = len(grid), len(grid[0])

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def find_symbol(grid, symbol):
    """Finds a symbol that appears once, like start, end, etc..."""
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == symbol:
                return (x, y)

deltas = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

# adj_dirs = {
#     '^': ['>', '<'],
#     '>': ['^', 'v'],
#     'v': ['>', '<'],
#     '<': ['^', 'v'],
# }

# opp_dir = {
#     '^': 'v',
#     '>': '<',
#     'v': '^',
#     '<': '>',
# }

xi, yi = find_symbol(grid, 'S')
xf, yf = find_symbol(grid, 'E')
grid[yi][xi] = 0
grid[yf][xf] = '.'
t1 = time.time()

step = 0
x, y = xi, yi
while True:
    if (x, y) == (xf, yf):
        print(step)
        break
    step += 1
    for (dx, dy) in deltas.values():
        new_x, new_y = x+dx, y+dy
        if grid[new_y][new_x] == '.':
            grid[new_y][new_x] = step
            x, y = new_x, new_y
            break

#dirs = list(deltas.keys())
cheats = defaultdict(int)
for y in range(1, n_rows-1):
    for x in range(1, n_cols-1):
        tile = grid[y][x]
        if tile != '#':
            continue
        adjacents = []
        for (dx, dy) in deltas.values():
            new_x, new_y = x+dx, y+dy
            new_tile = grid[new_y][new_x]
            if new_tile != '#':
                adjacents.append(new_tile)
        #print(x, y, adjacents)
        for j, tile1 in enumerate(adjacents):
            for tile2 in adjacents[j+1:]:
                cheats[abs(tile1-tile2) - 2] += 1

# saved_times = sorted(cheats.keys())
# for t in saved_times[1:]:
#     print (f'There are {cheats[t]} cheats that save {t} picoseconds')

ans_p1 = sum(n for t, n in cheats.items() if t >= 100)
print(f"Part 1 answer: {ans_p1}")
