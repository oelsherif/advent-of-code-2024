from copy import deepcopy
import time
with open("inputs/15.txt", "r") as File:
    lines = File.readlines()

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def calc_score(grid):
    score = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "O":
                score += 100*y + x
    return score

def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "@":
                return (x, y)

i = lines.index("\n")
orig_grid = [list(line[:-1]) for line in lines[:i]]
grid = deepcopy(orig_grid)
instructions = ""
for line in lines[i+1:]:
    instructions += line[:-1]

deltas = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

t1 = time.time()

x, y = find_start(grid)
for step in instructions:
    dx, dy = deltas[step]
    new_x, new_y = x, y
    while True:
        new_x, new_y = new_x+dx, new_y+dy
        tile = grid[new_y][new_x]
        if tile == '#':
            break
        if tile == 'O':
            continue
        grid[new_y][new_x] = 'O'
        grid[y+dy][x+dx] = '@'
        grid[y][x] = '.'
        y, x = y+dy, x+dx
        break

ans_p1 = calc_score(grid)
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")