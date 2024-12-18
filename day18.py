import time
with open("inputs/18.txt", "r") as File:
    lines = File.readlines()

bytes = [tuple([int(num) for num in line.split(',')]) for line in lines]

def in_bounds(x, y):
    if x < 0 or x > width:
        return False
    if y < 0 or y > height:
        return False
    return True

n_fallen = 1024
width, height = 70, 70
target = (width, height)

deltas = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

def find_shortest_path():
    corrupted = bytes[:n_fallen]
    grid = [[False]*(width + 1) for _ in range(height+1)]
    for (x, y) in corrupted:
        grid[y][x] = True
    xi, yi = 0, 0
    grid[yi][xi] = True
    old_currents = [(xi, yi)]
    target = (width, height)
    i = 0
    while True:
        i += 1
        new_currents = []
        for (x, y) in old_currents:
            for dx, dy in deltas.values():
                new_x, new_y = x+dx, y+dy
                if not in_bounds(new_x, new_y):
                    continue
                if target == (new_x, new_y):
                    return i
                if not grid[new_y][new_x]:
                    grid[new_y][new_x] = True
                    new_currents.append((new_x, new_y))
        old_currents = new_currents.copy()

def has_path(n_fallen):
    corrupted = bytes[:n_fallen]
    grid = [[False]*(width + 1) for _ in range(height+1)]
    for (x, y) in corrupted:
        grid[y][x] = True
    xi, yi = 0, 0
    grid[yi][xi] = True
    old_currents = [(xi, yi)]
    target = (width, height)
    while old_currents:
        new_currents = []
        for (x, y) in old_currents:
            for dx, dy in deltas.values():
                new_x, new_y = x+dx, y+dy
                if not in_bounds(new_x, new_y):
                    continue
                if target == (new_x, new_y):
                    return True
                if not grid[new_y][new_x]:
                    grid[new_y][new_x] = True
                    new_currents.append((new_x, new_y))
        old_currents = new_currents.copy()
    return False

t1 = time.time()
ans_p1 = find_shortest_path()
t2 = time.time()

#n_iterations = 0
n_left, n_right = 0, len(bytes)
while (n_right - n_left) > 1:
    #n_iterations += 1
    n_mid = (n_left + n_right)//2
    if has_path(n_mid):
        n_left = n_mid
    else:
        n_right = n_mid

#print(n_iterations)
x_ans, y_ans = bytes[n_left]
ans_p2 = f'{x_ans},{y_ans}'

t3 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.3f}s")
