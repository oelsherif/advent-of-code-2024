with open("inputs/05.txt", "r") as File:
    lines = File.readlines()

i_break = lines.index('\n') #find the index of the linebreak
rules = [tuple(int(word) for word in line.split('|')) for line in lines[:i_break]]
updates = [[int(word) for word in line.split(',')] for line in lines[i_break+1:] ]

def check_update(update, rules) -> bool:
    '''checks if update follows ordering rules'''
    for i, page1 in enumerate(update):
        for page2 in update[i+1:]:
            if (page2, page1) in rules:
                return False
    return True

def fix_update(update, rules) -> list:
    '''sorts update according to ordering rules. Uses selection sort'''
    i, n = 0, len(update)
    while i < n:
        page1 = update[i]
        j = i + 1
        while j < n:
            page2 = update[j]
            if (page2, page1) in rules:
                update[i], update[j] = page2, page1
                break
            j += 1
        else:
            i += 1
    return update

ans_p1, ans_p2 = 0, 0
for update in updates:
    if check_update(update, rules):
        ans_p1 += update[len(update)//2]
    else:
        fixed_update = fix_update(update, rules)
        ans_p2 += fixed_update[len(update)//2]

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
