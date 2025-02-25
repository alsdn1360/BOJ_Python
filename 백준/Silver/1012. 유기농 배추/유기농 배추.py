import sys
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = sys.stdin.readline


def oob(nx, ny):
    if 0 <= nx < N and 0 <= ny < M:
        return True
    else:
        return False


def bfs(start, field):
    queue = deque([start])
    field[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if oob(nx, ny) and field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = 0


# main
T = int(input())

for test in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    worm_cnt = 0

    for cabbage in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                worm_cnt += 1
                bfs((i, j), field)

    print(worm_cnt)
