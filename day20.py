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

xi, yi = find_symbol(grid, 'S')
xf, yf = find_symbol(grid, 'E')
grid[yi][xi] = 0
grid[yf][xf] = '.'
t1 = time.time()

coords = {} #coordinates at each ns
step = 0
x, y = xi, yi
while True:
    coords[step] = (x, y)
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
def get_cheats():
    '''original part 1 method'''
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
    return cheats

def count_cheats(len_cheat, threshold):
    '''counts cheats that save more than threshhold, where len_cheat is the max allowed cheat'''
    count = 0
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i+threshold, n):
            x2, y2 = coords[j]
            man_dist = abs(x2 - x1) + abs(y2 - y1)
            if man_dist > len_cheat:
                continue
            time_saved = j - i - man_dist
            if time_saved >= threshold:
                count += 1
    return count

t1 = time.time()
ans_p1 = sum(n for t, n in get_cheats().items() if t >= 100)
t2 = time.time()

print ("METHOD 1. Part 1 Only")
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")

t1 = time.time()
ans_p1 = count_cheats(2, 100)
t2 = time.time()
ans_p2 = count_cheats(20, 100)
t3 = time.time()

print ("METHOD 2")
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.3f}s")
