from copy import deepcopy
from collections import defaultdict
import time

with open("inputs/06.txt", "r") as File:
    grid = [['@'] + list(line[:-1]) + ['@'] for line in File]

def print_grid(grid):
    for row in grid:
        print(''.join(row))

n_cols = len(grid[0])
grid = [['@'] * n_cols] + grid + [['@'] * n_cols]
n_rows = len(grid)
        
deltas = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

original_grid = deepcopy(grid)

#find starting position
for y0, row in enumerate(grid):
    for x0, char in enumerate(row):
        if char == '^':
            break
    if char == '^':
        break

x, y, dir = x0, y0, '^'
visited = []
ans_p1 = 0
while True:
    if grid[y][x] == '@':
        break
    if grid[y][x] != 'X':
        grid[y][x] = 'X'
        visited.append((x, y)) ##gets co-ords we can add an obstacle in for part 2
        ans_p1 += 1
    dx, dy = deltas[dir]
    new_x, new_y = x + dx, y + dy
    while grid[new_y][new_x] == '#':
        dir = turn_right[dir]
        dx, dy = deltas[dir]
        new_x, new_y = x + dx, y + dy
    x, y = new_x, new_y

print(f"Part 1 answer: {ans_p1}")

def is_loop(obstacle, grid) -> bool:
    x_obstacle, y_obstace = obstacle
    grid[y_obstace][x_obstacle] = '#'
    x, y, dir = x0, y0, '^'
    past_dirs = defaultdict(list) #the directions each previous tile was visited
    while True:
        if grid[y][x] == '@':
            return False
        if grid[y][x] == 'X' and dir in past_dirs[(x, y)]:
            return True
        if grid[y][x] != 'X':
            grid[y][x] = 'X'
        past_dirs[(x, y)].append(dir)
        dx, dy = deltas[dir]
        new_x, new_y = x + dx, y + dy
        while grid[new_y][new_x] == '#':
            dir = turn_right[dir]
            dx, dy = deltas[dir]
            new_x, new_y = x + dx, y + dy
        x, y = new_x, new_y

ans_p2 = 0
t1 = time.time()
for obstacle in visited[1:]:
    grid = deepcopy(original_grid)
    if is_loop(obstacle, grid):
        ans_p2 += 1
t2 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t2 - t1:.2f}s")
