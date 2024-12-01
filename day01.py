from collections import Counter

with open("inputs/01.txt", "r") as File:
    lines = File.readlines()

arr1, arr2 = [], []
for line in lines:
    a, b = line.split()
    arr1.append(int(a))
    arr2.append(int(b))

arr1.sort()
arr2.sort()

ans_p1 = sum(abs(a-b) for a, b in zip(arr1, arr2))
print(f"Part 1 answer: {ans_p1}")

freq_2 = Counter(arr2)
ans_p2 = sum(num * freq_2[num] for num in arr1)
print(f"Part 2 answer: {ans_p2}")
