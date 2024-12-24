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

def get_numpad_presses(s):
    '''returns list of all possible sequences to replicate a numpad string s'''
    old_sequences = ['']
    prev_char = 'A'
    for char in s:
        new_sequences = []
        for path in numpad_paths[(prev_char, char)]:
            for sequence in old_sequences:
                new_sequences.append(sequence + path)
        old_sequences = new_sequences[:]
        prev_char = char
    return new_sequences

def get_keypad_presses(s):
    '''returns list of all possible sequences to replicate a keypad string s'''
    old_sequences = ['']
    prev_char = 'A'
    for char in s:
        new_sequences = []
        for path in keypad_paths[(prev_char, char)]:
            for sequence in old_sequences:
                new_sequences.append(sequence + path)
        old_sequences = new_sequences[:]
        prev_char = char
    return new_sequences

def get_layered_man_dist(string, n_layers):
    old_strings = [string]
    for _ in range(n_layers):
        new_strings = []
        for s in old_strings:
            new_strings += get_keypad_presses(s)
        new_lens = [len(s) for s in new_strings]
        min_len = min(new_lens)
        old_strings = [s for s, len in zip(new_strings, new_lens) if len == min_len]
    return min([get_man_dist(s) for s in old_strings])

def get_optimum_path_numpad(s):
    path = ''
    prev_char = 'A'
    for char in s:
        path += numpad_shortest_path[(prev_char, char)]
        prev_char = char
    return path

# def get_optimum_path_keypad(s, n = 1):
#     path = ''
#     prev_char = 'A'
#     for char in s:
#         path += keypad_shortest_path[(prev_char, char)]
#         prev_char = char
#     if n:
#         return get_optimum_path_keypad(path, n-1)
#     return path

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
        paths = get_paths(char1, char2, numpad_grid, numpad_loc)
        len_paths = [get_man_dist(path) for path in paths]
        min_len = min(len_paths)
        numpad_paths[(char1, char2)] = [path for path, len in zip(paths, len_paths) if len == min_len]

for char1 in keypad_chars:
    for char2 in keypad_chars:
        paths = get_paths(char1, char2, keypad_grid, keypad_loc)
        len_paths = [get_man_dist(path) for path in paths]
        min_len = min(len_paths)
        keypad_paths[(char1, char2)] = [path for path, len in zip(paths, len_paths) if len == min_len]

n_layers = 3
numpad_shortest_path = {}
keypad_shortest_path = {}
for char1 in numpad_chars:
    for char2 in numpad_chars:
        paths = numpad_paths[(char1, char2)]
        len_paths = [get_layered_man_dist(path, n_layers) for path in paths]
        min_len = min(len_paths)
        numpad_shortest_path[(char1, char2)] = [path for path, len in zip(paths, len_paths) if len == min_len][0]

for char1 in keypad_chars:
    for char2 in keypad_chars:
        paths = keypad_paths[(char1, char2)]
        len_paths = [get_layered_man_dist(path, n_layers) for path in paths]
        min_len = min(len_paths)
        keypad_shortest_path[(char1, char2)] = [path for path, len in zip(paths, len_paths) if len == min_len][0]

keypad_len_shortest_path = {}
keypad_len_shortest_path[1] = {}
for char1 in keypad_chars:
    for char2 in keypad_chars:
        keypad_len_shortest_path[1][(char1, char2)] = keypad_man_dist[(char1, char2)] + 1
for i in range(2, 26):
    keypad_len_shortest_path[i] = {}
    for char1 in keypad_chars:
        for char2 in keypad_chars:
            len_path = 0
            path = keypad_shortest_path[(char1, char2)]
            prev_char = 'A'
            for char in path:
                len_path += keypad_len_shortest_path[i-1][(prev_char, char)]
                prev_char = char 
            keypad_len_shortest_path[i][(char1, char2)] = len_path

def get_len_shortest_path(s, n):
    length = 0
    prev_char = 'A'
    for char in s:
        length += keypad_len_shortest_path[n][(prev_char, char)]
        prev_char = char
    return length

def calculate_complexity(codes, n_robots):
    complexity = 0
    for code in codes:
        s1 = get_optimum_path_numpad(code)
        len_seq = get_len_shortest_path(s1, n_robots)
        code_int = int(code[:-1])
        complexity += len_seq * code_int
    return complexity

ans_p1 = calculate_complexity(codes, 2)
ans_p2 = calculate_complexity(codes, 25)
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t2 - t1:.3f}s")
