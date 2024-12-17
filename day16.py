from copy import deepcopy
import time
import bisect
import random
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

###Step 1: Find Intersections
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
            edge_cost[(xi, yi, opp_dir[dir2])][(xi, yi, dir1)] = 1000

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

###Step 2: Make a network
edge_steps = {}
for node in nodes:
    cost = 0
    x, y, dir = node
    old_x, old_y, old_dir = x, y, dir
    dx, dy = deltas[dir]
    steps = []
    while True:
        steps.append((x, y, dir))
        new_x, new_y = x + dx, y + dy
        if grid[new_y][new_x] == 'X':
            edge_cost[node][(new_x, new_y, dir)] = cost + 1
            steps.append((new_x, new_y, dir))
            edge_steps[((old_x, old_y, old_dir), (new_x, new_y, dir))] = steps
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

###Step 3: Find one shortest path
current_nodes = [(xi, yi, '>')]
current_costs = [0]
prev_nodes = set()
while True:
    current_node = current_nodes.pop(0)
    current_cost = current_costs.pop(0)
    if current_node in prev_nodes:
        continue
    prev_nodes.add(current_node)
    x, y, _ = current_node
    if (x, y) == (xf, yf):
        ans_p1 = current_cost
        break
    for new_node, cost in edge_cost[current_node].items():
        new_cost = current_cost + cost
        i = bisect.bisect_left(current_costs, new_cost)
        current_costs.insert(i, new_cost)
        current_nodes.insert(i, new_node)

t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")

###Step 4: Find all tiles along shortest paths

arbitrary_n = 50
winning_tiles = set()
for _ in range(arbitrary_n):
    current_nodes = [(xi, yi, '>')]
    current_costs = [0]
    current_paths = [[(xi, yi, '>')]]
    winning_paths = []
    prev_nodes = set()
    while True:
        current_node = current_nodes.pop(0)
        current_cost = current_costs.pop(0)
        current_path = current_paths.pop(0)
        if current_cost > ans_p1:
            break
        x, y, dir = current_node
        if current_node in prev_nodes:
            continue
        prev_nodes.add(current_node)
        if (x, y) == (xf, yf):
            break
        for new_node, cost in edge_cost[current_node].items():
            new_cost = current_cost + cost
            new_x, new_y, new_dir = new_node
            new_path = current_path[:]
            new_path.append((new_x, new_y, new_dir))
            if bool(random.getrandbits(1)):
                i = bisect.bisect_left(current_costs, new_cost)
            else:
                i = bisect.bisect_right(current_costs, new_cost)
            current_costs.insert(i, new_cost)
            current_nodes.insert(i, new_node)
            current_paths.insert(i, new_path)

    #winning_tiles = set()
    for i in range(len(current_path) - 1):
        x1, y1, dir1 = current_path[i]
        x2, y2, dir2 = current_path[i+1]
        if (x1, y1) == (x2, y2):
            continue
        for (x, y, dir) in edge_steps[(x1, y1, dir1), (x2, y2, dir2)]:
            winning_tiles.add((x, y))

# for (x, y) in winning_tiles:
#     grid[y][x] = 'O'
#print_grid(grid)

ans_p2 = len(winning_tiles)
t3 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.2f}s")
