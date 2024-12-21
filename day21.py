from copy import deepcopy
import time
from collections import defaultdict
with open("inputs/21_test.txt", "r") as File:
    codes = [line[:-1] for line in File]

with open("extras/21_numpad.txt", "r") as File:
    numpad = [line[:-1] for line in File]

with open("extras/21_keypad.txt", "r") as File:
    keypad = [line[:-1] for line in File]

numpad_loc, keypad_loc = {}, {}
for y, row in enumerate(numpad):
    for x, char in enumerate(row):
        numpad_loc[char] = (x, y)

for y, row in enumerate(keypad):
    for x, char in enumerate(row):
        keypad_loc[char] = (x, y)

def get_numpad_presses(s):
    presses = ''
    prev_char = 'A'
    for char in s:
        x1, y1 = numpad_loc[prev_char]
        x2, y2 = numpad_loc[char]
        if y2 > y1:
            if x2 > x1:
                presses += '>' * (x2-x1)
            else:
                presses += '<' * (x1-x2)
            presses += 'v' * (y2-y1)
        else:
            presses += '^' * (y1-y2)
            if x2 > x1:
                presses += '>' * (x2-x1)
            else:
                presses += '<' * (x1-x2)
        presses += 'A'
        prev_char = char
    return presses

def get_keypad_presses(s, n):
    presses = ''
    prev_char = 'A'
    for char in s:
        x1, y1 = keypad_loc[prev_char]
        x2, y2 = keypad_loc[char]
        if y2 > y1:
            presses += 'v' * (y2-y1)
            if x2 > x1:
                presses += '>' * (x2-x1)
            else:
                presses += '<' * (x1-x2)
        else:
            if x2 > x1:
                presses += '>' * (x2-x1)
            else:
                presses += '<' * (x1-x2)
            presses += '^' * (y1-y2)
        presses += 'A'
        prev_char = char
    if n:
        return get_keypad_presses(presses, n-1)
    return presses

ans_p1 = 0
for code in codes:
    s1 = get_numpad_presses(code)
    s2 = get_keypad_presses(s1, 1)

t1 = time.time()
ans_p1 = 0
for code in codes:
    s1 = get_numpad_presses(code)
    s2 = get_keypad_presses(s1, 1)
    code_int = int(code[:-1])
    len2 = len(s2)
    print(code_int, len2)
    print(s2)
    ans_p1 += int(code[:-1]) * len(s2)
t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")
