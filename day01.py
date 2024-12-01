from collections import Counter

with open("inputs/01.txt", "r") as File:
    lines = [line.split() for line in File.readlines()]

arr1 = sorted(int(line[0]) for line in lines)
arr2 = sorted(int(line[1]) for line in lines)

ans_p1 = sum(abs(a-b) for a, b in zip(arr1, arr2))
print(f"Part 1 answer: {ans_p1}")

freq_2 = Counter(arr2)
ans_p2 = sum(num * freq_2[num] for num in arr1)
print(f"Part 2 answer: {ans_p2}")
