from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def in_bound(nx, ny):
    return 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1


# main
r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

p = []  # 공기청정기 행 위치

for i in range(r):
    if a[i][0] == -1:
        p.append(i)

queue = deque()

for _ in range(t):
    # 현재 미세먼지 위치
    for i in range(r):
        for j in range(c):
            if -1 <= a[i][j] <= 0:
                continue

            queue.append((i, j, a[i][j]))

    # 미세먼지 확산
    while queue:
        x, y, curr_dust = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny):
                a[nx][ny] += curr_dust // 5
                a[x][y] -= curr_dust // 5

    # 위쪽 공기청정기 가동(반시계 방향)
    temp_nxt = 0
    temp_prev = 0

    # 좌 -> 우
    for j in range(1, c):
        temp_nxt = a[p[0]][j]
        a[p[0]][j] = temp_prev
        temp_prev = temp_nxt

    # 하 -> 상
    for i in range(p[0] - 1, -1, -1):
        temp_nxt = a[i][c - 1]
        a[i][c - 1] = temp_prev
        temp_prev = temp_nxt

    # 우 -> 좌
    for j in range(c - 2, -1, -1):
        temp_nxt = a[0][j]
        a[0][j] = temp_prev
        temp_prev = temp_nxt

    # 상 -> 하
    for i in range(1, p[0]):
        temp_nxt = a[i][0]
        a[i][0] = temp_prev
        temp_prev = temp_nxt

    # 아래쪽 공기청정기(시계 방향)
    temp_nxt = 0
    temp_prev = 0

    # 좌 -> 우
    for j in range(1, c):
        temp_nxt = a[p[1]][j]
        a[p[1]][j] = temp_prev
        temp_prev = temp_nxt

    # 상 -> 하
    for i in range(p[1] + 1, r):
        temp_nxt = a[i][c - 1]
        a[i][c - 1] = temp_prev
        temp_prev = temp_nxt

    # 우 -> 좌
    for j in range(c - 2, -1, -1):
        temp_nxt = a[r - 1][j]
        a[r - 1][j] = temp_prev
        temp_prev = temp_nxt

    # 하 -> 상
    for i in range(r - 2, p[1], -1):
        temp_nxt = a[i][0]
        a[i][0] = temp_prev
        temp_prev = temp_nxt

# 공기청정기 부분 -2 보정
ans = 2

for i in range(r):
    for j in range(c):
        ans += a[i][j]

print(ans)
