import sys
from collections import deque

input = sys.stdin.readline
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(i, j, picture, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    color = picture[i][j]

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if oob(nx, ny) and not visited[nx][ny] and picture[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True


def check_area(picture):
    visited = [[False] * N for _ in range(N)]
    area = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                area += 1
                bfs(i, j, picture, visited)

    return area


# main
N = int(input())

picture = [list(input().strip()) for _ in range(N)]
blind_picture = [row[:] for row in picture]

for i in range(N):
    for j in range(N):
        if blind_picture[i][j] == "R":
            blind_picture[i][j] = "G"

normal_area = check_area(picture)
blind_area = check_area(blind_picture)

print(f"{normal_area} {blind_area}")
