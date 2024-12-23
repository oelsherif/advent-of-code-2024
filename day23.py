import time
from collections import defaultdict
with open("inputs/23.txt", "r") as File:
    lines = File.readlines()

t1 = time.time()
friends = defaultdict(set)
for line in lines:
    c1, c2 = line[0:2], line[3:5]
    friends[c1].add(c2)
    friends[c2].add(c1)

groups = set()
for comp1, friends1 in friends.items():
    if comp1[0] == 't':
        for comp2 in friends1:
            friends2 = friends[comp2]
            comps = friends1 & friends2
            for comp3 in comps:
                groups.add(tuple(sorted([comp1, comp2, comp3])))

t2 = time.time()
ans_p1 = len(groups)
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")


