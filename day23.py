import time
from collections import defaultdict
with open("inputs/23.txt", "r") as File:
    lines = File.readlines()

t1 = time.time()
connections = defaultdict(set)
for line in lines:
    c1, c2 = line[0:2], line[3:5]
    connections[c1].add(c2)
    connections[c2].add(c1)

groups = set()
for comp1, friends1 in connections.items():
    if comp1[0] == 't':
        for comp2 in friends1:
            friends2 = connections[comp2]
            comps = friends1 & friends2
            for comp3 in comps:
                groups.add(tuple(sorted([comp1, comp2, comp3])))

ans_p1 = len(groups)
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")

groups = set(tuple([comp]) for comp in connections.keys())
while len(groups) > 1:
    new_groups = set()
    for group in groups:
        friends_list = [connections[comp] for comp in group]
        common_friends = set.intersection(*friends_list)
        for friend in common_friends:
            new_groups.add(tuple(sorted(list(group) + [friend])))
    groups = new_groups.copy()
party = list(list(groups)[0])

ans_p2 = ','.join(party)
t3 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.3f}s")
