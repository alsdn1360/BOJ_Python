from collections import deque

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs(start):
    queue = deque([start])

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True

    cnt = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny] and campus[nx][ny] != "X":
                if campus[nx][ny] == "P":
                    cnt += 1

                queue.append((nx, ny))
                visited[nx][ny] = True

    return cnt if cnt > 0 else "TT"


# main
n, m = map(int, input().split())
campus = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            start = (i, j)

print(bfs(start))
