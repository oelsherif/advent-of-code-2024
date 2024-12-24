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
        return value
    return value

def get_numerical_value(char = 'z'):
    arr = sorted([wire for wire in wires if wire[0] == char])
    char_values = [get_value(c) for c in arr]
    return sum([num * 2**i for i, num in enumerate(char_values)])

t1 = time.time()
wires = list(wire_rules.keys()) + list(wire_values.keys())
ans_p1 = get_numerical_value('z')

# zees = sorted([wire for wire in wires if wire[0] == 'z'])
# suspects = []
# for z in zees:
#     print("---------")
#     print(z)
#     to_check = {z}
#     all_wires = {z}
#     for _ in range(2):
#         new_wires = set()
#         for wire in to_check:
#             for new_wire in [wire_rules[wire][0], wire_rules[wire][2]]:
#                 if new_wire[0] == 'x' or new_wire[0] == 'y':
#                     continue
#                 else:
#                     new_wires.add(new_wire)
#         to_check = new_wires - to_check
#         all_wires |= new_wires
#     rules = [wire_rules[wire] for wire in all_wires]
#     for wire in all_wires:
#         print(wire, wire_rules[wire])
#     operators = sorted([rule[1] for rule in rules])
#     if operators != ['AND', 'AND', 'OR', 'XOR', 'XOR']:
#         #print("SUSPICIONS ZZZZ")
#         suspects.append(z)
# print(suspects)

swaps = [('z11', 'rpv'), ('rpb', 'ctg'), ('z31', 'dmh'), ('dvq', 'z38')]
swapped_wires = []
for (w1, w2) in swaps:
    wire_rules[w1], wire_rules[w2] = wire_rules[w2], wire_rules[w1]
    swapped_wires += [w1, w2]

ans_p2 = ','.join(sorted(swapped_wires))
x_int = get_numerical_value('x')
y_int = get_numerical_value('y')
z_int = get_numerical_value('z')
print (x_int + y_int == z_int)

t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Time: {t2 - t1:.3f}s")



