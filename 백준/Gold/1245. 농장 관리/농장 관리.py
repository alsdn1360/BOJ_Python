from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs(x, y, curr_h):
    queue = deque([(x, y)])
    visited[x][y] = True

    is_peak = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny):
                if curr_h < farm[nx][ny]:
                    is_peak = False
                elif not visited[nx][ny] and curr_h == farm[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return 1 if is_peak else 0


# main
n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if farm[i][j] != 0 and not visited[i][j]:
            answer += bfs(i, j, farm[i][j])

print(answer)
