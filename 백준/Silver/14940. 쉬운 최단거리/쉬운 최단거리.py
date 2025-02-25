import sys
from collections import deque

input = sys.stdin.readline

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs(start, matrix, answer):
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    answer[start[0]][start[1]] = 0

    while queue:
        x, y, distance = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if oob(nx, ny) and not visited[nx][ny] and matrix[nx][ny] == 1:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
                answer[nx][ny] = distance + 1


# main
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1] * m for _ in range(n)]
start = (0, 0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start = (i, j)
        elif matrix[i][j] == 0:
            answer[i][j] = 0

bfs(start, matrix, answer)

for i in range(n):
    print(*answer[i])
