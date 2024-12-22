import time
from collections import defaultdict
with open("inputs/22.txt", "r") as File:
    secrets = [int(line) for line in File]

def step_1(num):
    num ^= (num*64)
    num %= 16777216
    return num

def step_2(num):
    num ^= (num//32)
    num %= 16777216
    return num

def step_3(num):
    num ^= (num*2048)
    num %= 16777216
    return num

def evolve_secret(num):
    return step_3(step_2(step_1(num)))

t1 = time.time()
secret_changes = []
secret_evolution = []
for num in secrets:
    changes = []
    evolution = []
    for _ in range(2000):
        new_num = evolve_secret(num)
        evolution.append(new_num)
        change = new_num%10 - num%10
        changes.append(change)
        num = new_num
    secret_changes.append(changes)
    secret_evolution.append(evolution)

ans_p1 = sum(sequence[-1] for sequence in secret_evolution)
print(f"Part 1 answer: {ans_p1}")

sequence_bananas = defaultdict(int) #total number of bananas for sequence
for (changes, evolution) in zip(secret_changes, secret_evolution):
    sequences = set()
    for j in range(4, len(changes)):
        sequence = tuple(changes[j-4:j])
        if sequence in sequences:
            continue
        sequences.add(sequence)
        sequence_bananas[sequence] += evolution[j-1]%10
ans_p2 = max(sequence_bananas.values())
t2 = time.time()
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t2 - t1:.3f}s")
