import time
with open("inputs/25.txt", "r") as File:
    lines = [line[:-1] for line in File.readlines()]

def do_fit(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

t1 = time.time()
i = 0
locks, keys = [], []
while i < len(lines):
    grid = lines[i:i+7]
    cols = [[row[j] for row in grid][1:6] for j in range(5)]
    arr = [col.count('#') for col in cols]
    if grid[0] == '#####':
        locks.append(arr)
    else:
        keys.append(arr)
    i += 8

ans = 0
for key in keys:
    for lock in locks:
        ans += do_fit(key, lock)
t2 = time.time()
print(f"Answer: {ans}")
print(f"Time: {t2 - t1:.3f}s")
