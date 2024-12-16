from copy import deepcopy
import time
with open("inputs/15.txt", "r") as File:
    lines = File.readlines()

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def calc_score(grid, box_tile):
    score = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == box_tile:
                score += 100*y + x
    return score

def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '@':
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

ans_p1 = calc_score(grid, 'O')
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")

def widen_row(row):
    new_row = []
    for tile in row:
        if tile == "@":
            new_row += ["@", "."]
        elif tile == "O":
            new_row += ["[", "]"]
        else:
            new_row += [tile, tile]
    return new_row

def widen_grid(grid):
    return [widen_row(row) for row in grid]

grid = widen_grid(orig_grid)

x, y = find_start(grid)
for step in instructions:
    #print_grid(grid)
    #print(step)
    if step == '>':
        row = grid[y]
        new_x = x
        while True:
            new_x += 1
            tile = row[new_x]
            if tile == '#':
                break
            if tile in ['[', ']']:
                continue
            grid[y] = row[:x] + ["."] + ["@"] + row[x+1:new_x] + row[new_x+1:]
            x += 1
            break
        continue
    if step == '<':
        row = grid[y]
        new_x = x
        while True:
            new_x -= 1
            tile = row[new_x]
            if tile == '#':
                break
            if tile in ['[', ']']:
                continue
            grid[y] = row[:new_x] + row[new_x+1:x] + ["@"] + ["."] + row[x+1:]
            x -= 1
            break
        continue
    _, dy = deltas[step]
    boxes = {y: [x]} #includes robot
    old_y = y
    while True:
        new_y = old_y + dy
        row = grid[new_y]
        old_boxes = boxes[old_y] #location of boxes/robots       
        new_boxes = []
        found_wall = False
        for i in old_boxes:
            if row[i] == '#':
                found_wall = True
            if row[i] == '[':
                new_boxes += [i, i+1]
            if row[i] == ']':
                new_boxes += [i-1, i]
        if found_wall:
            break
        boxes[new_y] = new_boxes
        if new_boxes:
            old_y = new_y
            continue
        for y2 in range(new_y, y, -dy):
            y1 = y2 - dy
            boxes1, boxes2 = boxes[y1], boxes[y2]
            for i in boxes2:
                grid[y2][i] = '.'
            for i in boxes1:
                grid[y2][i] = grid[y1][i]
        grid[y][x] = '.'
        y += dy
        break
#print_grid(grid)

ans_p2 = calc_score(grid, '[')
t3 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.2f}s")

