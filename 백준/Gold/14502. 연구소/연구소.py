from itertools import combinations
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def check_s_area(visited):
    s_area = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                s_area += 1

    return s_area


def bfs(walls, virus, n_walls):
    queue = deque((virus))

    visited = [[False for _ in range(m)] for _ in range(n)]

    for x, y in walls:
        visited[x][y] = True

    for x, y in virus:
        visited[x][y] = True

    for x, y in n_walls:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return check_s_area(visited)


# main
n, m = map(int, input().split())
lap = [list(map(int, input().split())) for _ in range(n)]

empty = []
walls = []
virus = []

for i in range(n):
    for j in range(m):
        if lap[i][j] == 0:
            empty.append((i, j))
        elif lap[i][j] == 1:
            walls.append((i, j))
        elif lap[i][j] == 2:
            virus.append((i, j))

ans = 0

# 빈 칸에 벽을 세울 수 있는 경우의 수 구하기
for n_walls in combinations(empty, 3):
    ans = max(ans, bfs(walls, virus, n_walls))

print(ans)
