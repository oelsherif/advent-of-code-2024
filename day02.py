with open("inputs/02.txt", "r") as File:
    lines = [[int(word) for word in line.split()] for line in File.readlines()]

def check_report(report):
    diff = report[1] - report[0]
    if diff > 0:
        allowed = [1, 2, 3]
    else:
        allowed = [-1, -2, -3]
    for i in range(1, len(report)):
        if report[i] - report[i-1] not in allowed:
            return False
    return True

ans_p1 = 0
for line in lines:
    ans_p1 += check_report(line)

print(f"Part 1 answer: {ans_p1}")

ans_p2 = 0
for line in lines:
    if check_report(line):
        ans_p2 += 1
        continue
    for i in range(len(line)):
        if check_report(line[:i] + line[i+1:]):
            ans_p2 += 1
            break
print(f"Part 2 answer: {ans_p2}")
    