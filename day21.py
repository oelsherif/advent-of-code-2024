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
            presses += '>' * (y2-y1)
        else:
            presses += '^' * (y1-y2)
        if x2 > x1:
            presses += '>' * (x2-x1)
        else:
            presses += '<' * (x1-x2)
        presses += 'A'
        prev_char = char
    return presses

#print(get_numpad_presses('029A'))
        