import time
with open("inputs/21.txt", "r") as File:
    codes = [line[:-1] for line in File]

with open("extras/21_numpad.txt", "r") as File:
    numpad_grid = [line[:-1] for line in File]

with open("extras/21_keypad.txt", "r") as File:
    keypad_grid = [line[:-1] for line in File]

deltas = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

numpad_loc, keypad_loc = {}, {}
for y, row in enumerate(numpad_grid):
    for x, char in enumerate(row):
        numpad_loc[char] = (x, y)

for y, row in enumerate(keypad_grid):
    for x, char in enumerate(row):
        keypad_loc[char] = (x, y)

def get_dirs(x1, y1, x2, y2):
    dirs = []
    if x2 > x1:
        dirs.append('>')
    elif x1 > x2:
        dirs.append('<')
    if y2 > y1:
        dirs.append('v')
    elif y1 > y2:
        dirs.append('^')
    return dirs
    
def get_paths(char1, char2, grid, locs):
    '''return all strings of valid paths between char1 and char2'''
    x1, y1 = locs[char1]
    x2, y2 = locs[char2]
    dirs = get_dirs(x1, y1, x2, y2)
    if not dirs:
        return ['A']
    man_dist = abs(x2-x1) + abs(y2-y1)
    old_positions = [(x1, y1)]
    old_paths = ['']
    for _ in range(man_dist):
        new_positions = []
        new_paths = []
        for position, path in zip(old_positions, old_paths):
            x, y = position
            for dir in dirs:
                dx, dy = deltas[dir]
                new_x, new_y = x + dx, y + dy
                if grid[new_y][new_x] == '#':
                    continue
                new_positions.append((new_x, new_y))
                new_paths.append(path + dir)
        old_positions = new_positions[:]
        old_paths = new_paths[:]
    return [path + 'A' for path, position in zip(new_paths, new_positions) if position == (x2, y2)]

def get_man_dist(s):
    '''return the Manhattan distance for traversing a sequence on a keypad'''
    total_man_dist = 0
    prev_char = 'A'
    for char in s:
        total_man_dist += keypad_man_dist[(prev_char, char)]
        prev_char = char
    return total_man_dist

def get_shortest_path(char1, char2, grid, locs):
    paths = get_paths(char1, char2, grid, locs)
    dists = [get_man_dist(path) for path in paths]
    i = dists.index(min(dists))
    return paths[i]

def get_shortest_sequence_numpad(s):
    '''given a sequence on a numpad, return one shortest keypad sequence to do it'''
    sequence = ''
    prev_char = 'A'
    for char in s:
        sequence += get_shortest_path(prev_char, char, numpad_grid, numpad_loc)
        prev_char = char
    return sequence

# def get_shortest_sequence_keypad(s):
#     '''given a sequence on a keypad, and the number of robots, return one shortest keypad sequence to do it'''
#     sequence = ''
#     prev_char = 'A'
#     for char in s:
#         sequence += get_shortest_path(prev_char, char, keypad_grid, keypad_loc)
#         prev_char = char
#     return sequence


def get_shortest_sequence_keypad(s, n_robots):
    '''given a sequence on a keypad, and the number of robots, return one shortest keypad sequence to do it'''
    sequence = ''
    prev_char = 'A'
    for char in s:
        sequence += get_shortest_path(prev_char, char, keypad_grid, keypad_loc)
        prev_char = char
    if n_robots:
        return get_shortest_sequence_keypad(sequence, n_robots-1)
    return sequence

    
t1 = time.time()

numpad_chars = '0123456789A'
keypad_chars = '<>^vA'

keypad_man_dist = {}

for char1 in keypad_chars:
    x1, y1 = keypad_loc[char1]
    for char2 in keypad_chars:
        x2, y2 = keypad_loc[char2]
        keypad_man_dist[(char1, char2)] = abs(x2-x1) + abs(y2-y1)

numpad_paths = {}
keypad_paths = {}
for char1 in numpad_chars:
    for char2 in numpad_chars:
        numpad_paths[(char1, char2)] = get_paths(char1, char2, numpad_grid, numpad_loc)

for char1 in keypad_chars:
    for char2 in keypad_chars:
        keypad_paths[(char1, char2)] = get_paths(char1, char2, keypad_grid, keypad_loc)

keypad_shortest_path = {}
for char1 in keypad_chars:
    for char2 in keypad_chars:
        keypad_shortest_path[(char1, char2)] = get_shortest_path(char1, char2, keypad_grid, keypad_loc)

# print(get_shortest_sequence_numpad('029A'))
# print(get_shortest_sequence_keypad('<A^A>^^AvvvA', 1))
# print(len(get_shortest_sequence_keypad('<A^A>^^AvvvA', 24)))
# robot_keypad_dist = {}
# robot_keypad_dist[1] = keypad_man_dist
# for i in range(2, 26):
#     robot_keypad_dist[i] = {}
#     for char1 in keypad_chars:
#         for char2 in keypad_chars:
#             path = keypad_shortest_path[(char1, char2)]
#             length = 0
#             prev_char = 'A'
#             for char in path:
#                 length += robot_keypad_dist[i-1][(prev_char, char)] + 1
#                 prev_char = char
#             robot_keypad_dist[i][(char1, char2)] = length

t1 = time.time()
code = '456A'
keypad_presses = get_shortest_sequence_numpad(code)
ans = get_shortest_sequence_keypad(keypad_presses, 1)

print(len(ans))
t2 = time.time()
