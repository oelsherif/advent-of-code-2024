from collections import defaultdict

with open("inputs/08.txt", "r") as File:
    grid = [line[:-1] for line in File]

n_rows, n_cols = len(grid), len(grid[0])
def is_in_range(x, y) -> bool:
    if x < 0 or x >= n_cols:
        return False
    if y < 0 or y >= n_rows:
        return False
    return True

ant_locs = defaultdict(list)
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char != '.':
            ant_locs[char].append((x, y))

def is_in_grid(x, y) -> bool:
    if x < 0 or x >= n_cols:
        return False
    if y < 0 or y >= n_rows:
        return False
    return True

def pot_antinodes_p1(x1, y1, x2, y2):
    dx, dy = x2-x1, y2-y1
    potential_antinodes = [(x1-dx, y1-dy), (x2+dx, y2+dy)]
    new_antinodes = []
    ##The following part didn't end up mattering
    ####################
    if dx%3 == 0 and dy%3 == 0:
        potential_antinodes.append((x1+dx//3, y1+dy//3))
        potential_antinodes.append((x2-dx//3, y2-dy//3))
    for (x, y) in potential_antinodes:
        if is_in_grid(x, y):
            new_antinodes.append((x,y))
    ####################
    return new_antinodes

def pot_antinodes_p2(x1, y1, x2, y2):
    dx, dy = x2-x1, y2-y1
    new_antinodes = [(x1, y1), (x2, y2)]
    new_x, new_y = x1, y1
    while True:
        new_x -= dx
        new_y -= dy
        if is_in_grid(new_x, new_y):
            new_antinodes.append((new_x, new_y))
        else:
            break
    new_x, new_y = x2, y2
    while True:
        new_x += dx
        new_y += dy
        if is_in_grid(new_x, new_y):
            new_antinodes.append((new_x, new_y))
        else:
            break
    return new_antinodes

antinodes_p1 = set()
antinodes_p2 = set()
for ant, locs in ant_locs.items():
    for i, (x1, y1) in enumerate(locs):
        for (x2, y2) in locs[i+1:]:
            antinodes_p1.update(pot_antinodes_p1(x1, y1, x2, y2))
            antinodes_p2.update(pot_antinodes_p2(x1, y1, x2, y2))
ans_p1 = len(antinodes_p1)
print(f"Part 1 answer: {ans_p1}")
ans_p2 = len(antinodes_p2)
print(f"Part 2 answer: {ans_p2}")
