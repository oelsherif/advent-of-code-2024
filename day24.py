import time
with open("inputs/24.txt", "r") as File:
    lines = File.readlines()

i = lines.index("\n")
wire_values = {}
for line in lines[:i]:
    wire, value = line[:3], int(line[-2])
    wire_values[wire] = value

wire_rules = {}
for line in lines[i+1:]:
    words = line.split()
    wire_rules[words[4]] = words[:3]

def calc_value(wire) -> int:
    w1, op, w2 = wire_rules[wire]
    w1, w2 = get_value(w1), get_value(w2)
    if op == 'AND':
        return w1 and w2
    if op == 'OR':
        return w1 or w2
    if op == 'XOR':
        return w1 ^ w2

def get_value(wire) -> int:
    value = wire_values.get(wire, None)
    if value == None:
        value = calc_value(wire)
        wire_values[wire] = value
        return value
    return value

t1 = time.time()
wires = list(wire_rules.keys()) + list(wire_values.keys())
zees = sorted([wire for wire in wires if wire[0] == 'z'])
z_values = [get_value(z) for z in zees]
ans_p1 = sum([num * 2**i for i, num in enumerate(z_values)])
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 1 time: {t2 - t1:.3f}s")

