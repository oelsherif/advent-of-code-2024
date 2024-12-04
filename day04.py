with open("inputs/04.txt", "r") as File:
    grid = [line[:-1] for line in File.readlines()]

n_rows, n_cols = len(grid), len(grid[0])
cols = [''.join(row[i] for row in grid) for i in range(n_cols)]

top_starts = [(0, j) for j in range(n_cols)]
left_starts = [(i, 0) for i in range(1, n_rows)] #excluding top_left corner
right_starts = [(i, n_cols-1) for i in range(1, n_rows)] #excluding top_right corner
neg_diags = []
for i, j in top_starts + left_starts:
    diag = ''
    while i < n_rows and j < n_cols:
        diag += grid[i][j]
        i += 1
        j += 1
    neg_diags.append(diag)
pos_diags = []
for i, j in top_starts + right_starts:
    diag = ''
    while i < n_rows and j >= 0:
        diag += grid[i][j]
        i += 1
        j -= 1
    pos_diags.append(diag)

ans_p1 = 0
lines = grid + cols + neg_diags + pos_diags
for line in lines:
    ans_p1 += line.count('XMAS') + line.count('SAMX')
print(f"Part 1 answer: {ans_p1}")

ans_p2 = 0
for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
        if grid[i][j] != 'A':
            continue
        NW, NE = grid[i-1][j-1], grid[i-1][j+1]
        SW, SE = grid[i+1][j-1], grid[i+1][j+1]
        if NW == SE:
            continue
        if sorted([NW, NE, SW, SE]) == ['M', 'M', 'S', 'S']:
            ans_p2 += 1

print(f"Part 2 answer: {ans_p2}")


