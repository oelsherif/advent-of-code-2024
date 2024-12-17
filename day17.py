with open("inputs/17.txt", "r") as File:
    lines = File.readlines()

regs = [int(lines[i].split()[-1]) for i in range(3)]
program = [int(char) for char in lines[-1].split()[-1].split(',')]

def get_combo(operand):
    if operand == 7:
        print("YOU PROMISED THIS WON'T HAPPEN")
        return None
    if operand < 4:
        return operand
    return regs[operand - 4]

def adv(operand: int) -> None:
    """opcode 0"""
    regs[0] //= (2**get_combo(operand))

def bxl(operand: int) -> None:
    """opcode 1"""
    regs[1] ^= operand

def bst(operand: int) -> None:
    """opcode 2"""
    regs[1] = get_combo(operand)%8

def jnz(operand: int) -> None:
    """opcode 3"""
    global i
    if regs[0]:
        i = operand - 2

def bxc(operand: int) -> None:
    """opcode 4"""
    regs[1] ^= regs[2]

def out(operand: int) -> None:
    """opcode 5"""
    output.append(get_combo(operand)%8)

def bdv(operand: int) -> None:
    """opcode 6"""
    regs[1] = regs[0]//(2**get_combo(operand))

def cdv(operand: int) -> None:
    """opcode 7"""
    regs[2] = regs[0]//(2**get_combo(operand))

execute = {
    0: adv, 1: bxl, 2: bst, 3: jnz,
    4: bxc, 5: out, 6: bdv, 7: cdv,
}

i = 0
output = []
while i < len(program) - 1:
    opcode = program[i]
    operand = program[i+1]
    execute[opcode](operand)
    i += 2

ans_p1 = ','.join(str(num) for num in output)
print(f"Part 1 answer: {ans_p1}")

pot_As = [0]
n = len(program)
for j in range(1, n+1):
    required = program[n-j:n]
    new_As = []
    for a in pot_As:
        a *= 8
        for x in range(8):
            i = 0
            output = []
            regs = [a+x, 0, 0]
            while i < len(program) - 1:
                opcode = program[i]
                operand = program[i+1]
                execute[opcode](operand)
                i += 2
            if output == required:
                new_As.append(a+x)
            x += 1
    pot_As = new_As
ans_p2 = min(new_As)

print(f"Part 2 answer: {ans_p2}")

