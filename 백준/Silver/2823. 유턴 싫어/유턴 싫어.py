MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < r and 0 <= ny < c


# main
r, c = map(int, input().split())
village = [list(input()) for _ in range(r)]

is_possible = True

for x in range(r):
    for y in range(c):
        if village[x][y] == "X":
            continue

        adj_road_cnt = 0

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and village[nx][ny] == ".":
                adj_road_cnt += 1

        if adj_road_cnt <= 1:
            is_possible = False
            break

    if not is_possible:
        break

print(0) if is_possible else print(1)
