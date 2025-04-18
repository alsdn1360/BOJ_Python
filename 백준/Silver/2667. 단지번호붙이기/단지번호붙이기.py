from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(n, nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def bfs(n, apart, visited, i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if oob(n, nx, ny) and not visited[nx][ny] and apart[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt


# main
n = int(input())
apart = [list(map(int, input())) for _ in range(n)]

total_apart = 0  # 총 단지수
cnt_apart = []  # 각 단내 집의 수

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1 and not visited[i][j]:
            cnt_apart.append(bfs(n, apart, visited, i, j))
            total_apart += 1

cnt_apart.sort()

print(total_apart)
print(*cnt_apart, sep="\n")
