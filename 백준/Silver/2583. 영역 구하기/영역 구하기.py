from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < m and 0 <= ny < n


def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True

    area = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and paper[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return area


# main
m, n, k = map(int, input().split())

paper = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

area_cnt = 0
answer = []

for i in range(m):
    for j in range(n):
        if paper[i][j] == 0 and not visited[i][j]:
            area_cnt += 1
            answer.append(bfs(i, j))

answer.sort()

print(area_cnt)
print(*answer)
