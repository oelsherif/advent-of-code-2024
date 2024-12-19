import time
from collections import defaultdict
with open("inputs/19.txt", "r") as File:
    lines = File.readlines()

patterns = [word for word in lines[0][:-1].split(', ')]
designs = [line[:-1] for line in lines[2:]]

def count_options(design) -> int:
    ends = defaultdict(list) #ends[start] = [end1, end2, ...]
    n = len(design)
    for pattern in patterns:
        m = len(pattern)
        for i in range(n-m+1):
            if pattern == design[i:i+m]:
                ends[i].append(i+m)

    options = defaultdict(int) #number of options at each index
    options[0] = 1
    for i in range(n):
        for end in ends[i]:
            options[end] += options[i]
    return options[n]

t1 = time.time()
ans_p1, ans_p2 = 0, 0
for design in designs:
    n_options = count_options(design)
    ans_p1 += bool(n_options)
    ans_p2 += n_options
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t2 - t1:.3f}s")
