from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def check_all_ripe():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False

    return True


# main
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# bfs
queue = deque()
all_ripe_days = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    x, y, ripe_days = queue.popleft()

    all_ripe_days = max(all_ripe_days, ripe_days)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny) and box[nx][ny] == 0:
            queue.append((nx, ny, ripe_days + 1))
            box[nx][ny] = 1

print(all_ripe_days) if check_all_ripe() else print(-1)
