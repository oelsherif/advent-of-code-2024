with open("inputs/13.txt", "r") as File:
    lines = File.readlines()

offset = 10000000000000
mats_p1, mats_p2 = [], []
for i in range(0, len(lines), 4):
    line_A = lines[i]
    line_B = lines[i+1]
    line_C = lines[i+2]
    Ax = int(line_A[line_A.find('+'):line_A.find(',')])
    Ay = int(line_A[line_A.rfind('+'):])
    Bx = int(line_B[line_B.find('+'):line_B.find(',')])
    By = int(line_B[line_B.rfind('+'):])
    Cx = int(line_C[line_C.find('=')+1:line_C.find(',')])
    Cy = int(line_C[line_C.rfind('=')+1:])
    mats_p1.append([[Ax, Bx, Cx], [Ay, By, Cy]])
    mats_p2.append([[Ax, Bx, Cx+offset], [Ay, By, Cy+offset]])

def solve_mat(mat):
    """solves Ax + Bx = Cx, Ay + By = Cy
    returns None for non_integer solutions
    """
    Ax, Bx, Cx = mat[0]
    Ay, By, Cy = mat[1]
    det = Ax*By - Ay*Bx
    if det == 0:
        return None
    A_n = (By*Cx - Bx*Cy)/det
    B_n = (-Ay*Cx + Ax*Cy)/det
    A_n, B_n = round(A_n), round(B_n)
    if A_n*Ax + B_n*Bx == Cx and A_n*Ay + B_n*By == Cy:
        return [A_n, B_n]

def solve_all(mats):
    ans = 0
    for mat in mats:
        presses = solve_mat(mat)
        if not presses:
            continue
        A_n, B_n = presses
        ans += int((3 * A_n + B_n))
    return ans

ans_p1 = solve_all(mats_p1)
print(f"Part 1 answer: {ans_p1}")
ans_p2 = solve_all(mats_p2)
print(f"Part 2 answer: {ans_p2}")
