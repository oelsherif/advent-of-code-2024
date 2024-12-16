from copy import deepcopy
import time
import bisect
from collections import defaultdict
with open("inputs/16.txt", "r") as File:
    lines = File.readlines()

orig_grid = [list(line[:-1]) for line in lines]
grid = deepcopy(orig_grid)

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

adj_dirs = {
    '^': ['>', '<'],
    '>': ['^', 'v'],
    'v': ['>', '<'],
    '<': ['^', 'v'],
}

opp_dir = {
    '^': 'v',
    '>': '<',
    'v': '^',
    '<': '>',
}


xi, yi = find_symbol(grid, 'S')
xf, yf = find_symbol(grid, 'E')
grid[yi][xi] = 'X'
grid[yf][xf] = 'X'
t1 = time.time()

#Step 1: Find Intersections
turn_cost = 1000
move_cost = 1
edge_cost = defaultdict(dict) #score between two nodes

nodes = set()
possible_dirs = []
for dir, (dx, dy) in deltas.items():
    if grid[yi+dy][xi+dx] == '.':
        possible_dirs.append(dir)
    for dir2 in possible_dirs:
        nodes.add((xi, yi, dir2))
        for dir1 in adj_dirs[dir2]:
            edge_cost[(xi, yi, dir1)][(xi, yi, dir2)] = 1000

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '#':
            continue
        possible_dirs = []
        for dir, (dx, dy) in deltas.items():
            if grid[y+dy][x+dx] == '.':
                possible_dirs.append(dir)
        if len(possible_dirs) < 3:
            continue
        grid[y][x] = 'X'
        for dir2 in possible_dirs:
            nodes.add((x, y, dir2))
            for dir1 in adj_dirs[dir2]:
                if dir1 in possible_dirs:
                    edge_cost[(x, y, opp_dir[dir1])][(x, y, dir2)] = 1000

#Step 2: Make a network
for node in nodes:
    cost = 0
    x, y, dir = node
    dx, dy = deltas[dir]
    while True:
        new_x, new_y = x + dx, y + dy
        if grid[new_y][new_x] == 'X':
            edge_cost[node][(new_x, new_y, dir)] = cost + 1
            break
        if grid[new_y][new_x] == '.':
            cost += 1
            x, y = new_x, new_y
            continue
        if grid[new_y][new_x] == '#':
            for new_dir in adj_dirs[dir]:
                dx, dy = deltas[new_dir]
                new_x, new_y = x + dx, y + dy
                if grid[new_y][new_x] == '.':
                    cost += 1000
                    dir = new_dir
                    break
            else:
                break

#Step 3: Find paths
current_nodes = [(xi, yi, '>')]
current_costs = [0]
while True:
    current_node = current_nodes.pop(0)
    current_cost = current_costs.pop(0)
    #print(current_node, current_cost, len(current_nodes))
    x, y, _ = current_node
    if (x, y) == (xf, yf):
        ans_p1 = current_cost
        break
    for new_node, cost in edge_cost[current_node].items():
        new_cost = current_cost + cost
        if new_node in current_nodes:
            j = current_nodes.index(new_node)
            if new_cost >= current_costs[j]:
                continue

        i = bisect.bisect_left(current_costs, new_cost)
        current_costs.insert(i, new_cost)
        current_nodes.insert(i, new_node)

t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")

