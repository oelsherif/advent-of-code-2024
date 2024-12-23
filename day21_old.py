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
        return ['']
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
    return [path for path, position in zip(new_paths, new_positions) if position == (x2, y2)]

def get_keypad_presses(s):
    '''returns list of all possilbe sequences to get replicate string s'''
    old_sequences = ['']
    prev_char = 'A'
    for char in s:
        new_sequences = []
        for path in keypad_paths[(prev_char, char)]:
            for sequence in old_sequences:
                new_sequences.append(sequence + path + 'A')
        old_sequences = new_sequences[:]
        prev_char = char
    return new_sequences

def get_all_keypad_presses(string_list):
    all_sequences = []
    for s in string_list:
        all_sequences += get_keypad_presses(s)
    return all_sequences

def get_numpad_presses(s):
    '''returns list of all possilbe sequences to get replicate string s'''
    old_sequences = ['']
    prev_char = 'A'
    for char in s:
        new_sequences = []
        for path in numpad_paths[(prev_char, char)]:
            for sequence in old_sequences:
                new_sequences.append(sequence + path + 'A')
        old_sequences = new_sequences[:]
        prev_char = char
    return new_sequences

def shortest_seq_length(s):
    arr1 = get_numpad_presses(s)
    arr2 = get_all_keypad_presses(arr1)
    arr3 = get_all_keypad_presses(arr2)
    return min(len(arr) for arr in arr3)
    
t1 = time.time()

numpad_chars = '0123456789A'
keypad_chars = '<>^vA'
numpad_paths = {}
keypad_paths = {}

for char1 in numpad_chars:
    for char2 in numpad_chars:
        numpad_paths[(char1, char2)] = get_paths(char1, char2, numpad_grid, numpad_loc)

for char1 in keypad_chars:
    for char2 in keypad_chars:
        keypad_paths[(char1, char2)] = get_paths(char1, char2, keypad_grid, keypad_loc)

ans_p1 = 0
for code in codes:
    len_seq = shortest_seq_length(code)
    code_int = int(code[:-1])
    ans_p1 += len_seq * code_int

t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")
