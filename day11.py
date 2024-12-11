import time
from collections import Counter, defaultdict
with open("inputs/11.txt", "r") as File:
    line = File.readline().split()

def evolve(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    if (n := len(stone)) % 2 == 0:
        return [stone[:n//2], str(int(stone[n//2:]))]
    return[str(int(stone) * 2024)]

def evolve_dict(stones: dict[str, int]) -> dict[str, int]:
    new_dict = defaultdict(int)
    for stone, count in stones.items():
        for new_stone in evolve(stone):
            new_dict[new_stone] += count
    return new_dict

stones_freq = Counter(line)
n_p1, n_p2 = 25, 75
t1 = time.time()
for _ in range(n_p1):
    stones_freq = evolve_dict(stones_freq)
ans_p1 = sum(stones_freq.values())
t2 = time.time()
for _ in range(n_p1, n_p2):
    stones_freq = evolve_dict(stones_freq)
ans_p2 = sum(stones_freq.values())
t3 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.2f}s")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t3 - t2:.2f}s")



# stones = line[:]
# stones_dict = Counter(stones)
# t1 = time.time()
# n = 25
# for _ in range(n):
#     stones = evolve_list(stones)
# t2 = time.time()
# ans_p1 = len(stones)
# print(f"Part 1 answer: {ans_p1}")
# print(f"Part 1 time: {t2 - t1:.2f}s")

# n = 75
# for _ in range(n):
#     stones_dict = evolve_dict(stones_dict)
# t3 = time.time()
# ans_p2 = sum(stones_dict.values())
# print(f"Part 2 answer: {ans_p2}")
# print(f"Part 2 time: {t3 - t2:.2f}s")
