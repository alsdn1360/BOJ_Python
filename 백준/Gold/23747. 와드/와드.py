from collections import deque

# U, D, L, R
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(nr, nc):
    if 0 <= nr < R and 0 <= nc < C:
        return True
    else:
        return False


def ward(matrix, vision, ward_position):
    vision[ward_position[0]][ward_position[1]] = '.'
    
    queue = deque([(ward_position)])
    char_area = matrix[ward_position[0]][ward_position[1]]

    while queue:
        r, c = queue.popleft()

        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc

            if oob(nr, nc):
                if vision[nr][nc] == "#" and matrix[nr][nc] == char_area:
                    vision[nr][nc] = "."
                    queue.append((nr, nc))


def trip(matrix, start, records):
    vision = [["#" for _ in range(C)] for _ in range(R)]
    cur_r, cur_c = start

    for record in records:
        if record == "W":
            ward(matrix, vision, (cur_r, cur_c))
        else:
            if record == "U":
                cur_r -= 1
            elif record == "D":
                cur_r += 1
            elif record == "L":
                cur_c -= 1
            elif record == "R":
                cur_c += 1

    vision[cur_r][cur_c] = "."

    for dr, dc in MOVES:
        nr, nc = cur_r + dr, cur_c + dc

        if oob(nr, nc):
            if vision[nr][nc] == "#":
                vision[nr][nc] = "."

    return vision


# main
R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]
Hr, Hc = map(int, input().split())
records = input().strip()

answer = trip(matrix, (Hr - 1, Hc - 1), records)

for row in answer:
    print("".join(row))
