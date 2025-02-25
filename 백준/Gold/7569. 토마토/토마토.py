import sys
from collections import deque

input = sys.stdin.readline

MOVES = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]


def oob(nx, ny, nz):
    return 0 <= nx < H and 0 <= ny < N and 0 <= nz < M


def bfs(box):
    queue = deque()
    all_ripe_day = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    queue.append((i, j, k, 0))

    while queue:
        x, y, z, day = queue.popleft()
        all_ripe_day = max(all_ripe_day, day)

        for dx, dy, dz in MOVES:
            nx, ny, nz = x + dx, y + dy, z + dz

            if oob(nx, ny, nz) and box[nx][ny][nz] == 0:
                queue.append((nx, ny, nz, day + 1))
                box[nx][ny][nz] = 1

    return all_ripe_day


# main
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

all_ripe = True
answer = bfs(box)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                all_ripe = False
                break

if all_ripe:
    print(answer)
else:
    print(-1)
