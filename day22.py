import time
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

def evolve_secret(num, n):
    for _ in range(n):
        num = step_3(step_2(step_1(num)))
    return num

print(evolve_secret(123,10))
t1 = time.time()
ans_p1 = sum(evolve_secret(num, 2000) for num in secrets)
t2 = time.time()

print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")
