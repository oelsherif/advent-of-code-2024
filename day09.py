with open("inputs/09.txt", "r") as File:
    line = File.readline()[:-1]

def checksum_p1(line) -> int:
    i, j = 0, len(line) - 1
    left_id = 0
    right_id = j // 2
    pos = 0
    checksum = 0
    num_right = int(line[j])
    while i < j:
        num_left = int(line[i])
        for _ in range(num_left):
            checksum += left_id * pos
            pos += 1
        gap = int(line[i+1])
        for _ in range(gap):
            if not num_right:
                j -= 2
                right_id -= 1
                num_right = int(line[j])
            if j <= i:
                return checksum
            checksum += right_id * pos
            pos += 1
            num_right -= 1
        i += 2
        left_id += 1
    for _ in range(num_right):
        checksum += right_id * pos
        pos += 1
    return checksum

def file_checksum(pos, size, id) -> int:
    return id * size * (2*pos + size - 1) // 2

def checksum_p2(line) -> int:
    is_gap = False
    pos, id = 0, 0
    files, gaps = [], []
    for char in line:
        size = int(char)
        if is_gap:
            gaps.append((pos, size))
        else:
            files.append((pos, size, id))
            id += 1
        pos += size
        is_gap = not is_gap

    checksum = 0
    for (file_pos, file_size, file_id) in files[::-1]:
        added_to_checksum = False
        for i, (gap_pos, gap_size) in enumerate(gaps):
            if file_pos < gap_pos:
                break
            if file_size <= gap_size:
                checksum += file_checksum(gap_pos, file_size, file_id)
                gaps[i] = (gap_pos + file_size, gap_size - file_size)
                added_to_checksum = True
                break
        if not added_to_checksum:
            checksum += file_checksum(file_pos, file_size, file_id)
    return checksum

ans_p1 = checksum_p1(line)
print(f"Part 1 answer: {ans_p1}")
ans_p2 = checksum_p2(line)
print(f"Part 2 answer: {ans_p2}")
