with open("inputs/03.txt", "r") as File:
    lines = File.readlines()

def multiply_some_numbers(line):
    '''multiply numbers as described in the problem'''
    ans = 0
    last_i = 0
    while True:
        i = line.find('mul(', last_i)
        if i == -1:
            break
        j = line.find(')', i)
        last_i = i + 4
        if j == -1:
            break
        nums = line[i+4:j].split(',')
        if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
            ans += int(nums[0]) * int(nums[1])
    return ans

def remove_disabled(line):
    '''return a string with only the enabled parts'''
    i = line.find("don't()")
    new_line = line[:i]
    last_i = i
    while True:
        i = line.find("do()", last_i)
        if i == -1:
            break
        j = line.find("don't()", i)
        if j == -1:
            new_line += line[i+4:]
            break
        new_line += line[i+4:j]
        last_i = j
    return new_line

line = ''.join(lines)
ans_p1 = multiply_some_numbers(line)
print(f"Part 1 answer: {ans_p1}")

ans_p2 = multiply_some_numbers(remove_disabled(line))    
print(f"Part 2 answer: {ans_p2}")
