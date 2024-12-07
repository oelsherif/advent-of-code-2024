import time

with open("inputs/07.txt", "r") as File:
    lines = File.readlines()

results, terms_list = [], []
for line in lines:
    i = line.find(':')
    results.append(int(line[:i]))
    terms_list.append([int(word) for word in line[i+1:].split()])

def concat(num1, num2) -> int:
    return int(str(num1) + str(num2))

def is_solvable_p1(result, terms) -> bool:
    answers = {terms[0]}
    for term in terms[1:]:
        answers = (
            {num * term for num in answers} 
            | {num + term for num in answers}
        )
    return result in answers

def is_solvable_p2(result, terms) -> bool:
    answers = {terms[0]}
    for term in terms[1:]:
        answers = (
            {num * term for num in answers} 
            | {num + term for num in answers}
            | {concat(num,term) for num in answers}
        )
    return result in answers

t1 = time.time()
ans_p1 = sum(result for result, terms in zip(results, terms_list) if is_solvable_p1(result, terms))
ans_p2 = sum(result for result, terms in zip(results, terms_list) if is_solvable_p2(result, terms))
t2 = time.time()
print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
print(f"Part 2 time: {t2 - t1:.2f}s")
