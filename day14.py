import time
from collections import defaultdict
from functools import reduce 
from operator import mul
with open("inputs/14.txt", "r") as File:
    lines = File.readlines()

#width, height = 11, 7  #test_data
width, height = 101, 103  #real_data
T = 100

positions, velocities = [], []
for line in lines:
    p, v = line.split()
    x, y = [int(s) for s in p[2:].split(',')]
    positions.append((x, y))
    vx, vy = [int(s) for s in v[2:].split(',')]
    velocities.append((vx, vy))

def get_pos(t, pos, vel):
    """gets position after t seconds"""
    x0, y0 = pos
    vx0, vy0 = vel
    xf = x0 + t * vx0
    yf = y0 + t * vy0
    return (xf%width, yf%height)

def get_quadrant(pos):
    x, y = pos
    if x == x_mid or y == y_mid:
        return None
    return (int(x>x_mid), int(y>y_mid))

def count_quads(positions):
    quad_count = defaultdict(int)
    for pos in positions:
        quad = get_quadrant(pos)
        if quad:
            quad_count[quad] += 1
    return quad_count

x_mid, y_mid = width // 2, height // 2

t1 = time.time()
new_positions = [get_pos(T, pos, val) for pos, val in zip(positions, velocities)]
quad_count = count_quads(new_positions)
ans_p1 = reduce(mul, quad_count.values(), 1)
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")


t = 0
Found = False
while True:
    t += 1
    positions = [get_pos(1, pos, val) for pos, val in zip(positions, velocities)]
    grid = [['.']*width for _ in range(height)]
    for (x, y) in positions:
        grid[y][x] = 'X'
    for row in grid:
        if 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' in ''.join(row):
            Found = True
    if Found == True:
        break
ans_p2 = t
for row in grid:
    print(''.join(row))
t3 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.2f}s")
