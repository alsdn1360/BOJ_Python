from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < M and 0 <= ny < N


def bfs():
    queue = deque([(X, Y, H[X][Y], 0)])

    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[X][Y] = True

    for x, y, _ in T:
        visited[x][y] = True

    max_h = H[X][Y]
    min_t = float("inf")

    while queue:
        x, y, curr_h, curr_t = queue.popleft()

        if curr_h > max_h:
            max_h = curr_h
            min_t = curr_t
        elif curr_h == max_h:
            min_t = min(min_t, curr_t)

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny]:
                # 다음 시간에 화산쇄설류에 막혀있지 않다면 이동
                if curr_t + 1 < cover_pyroclast_times[nx][ny]:
                    queue.append((nx, ny, H[nx][ny], curr_t + 1))
                    visited[nx][ny] = True

    return max_h, min_t


# main
M, N, V = map(int, input().split())
X, Y = map(int, input().split())
X, Y = X - 1, Y - 1

H = [list(map(int, input().split())) for _ in range(M)]
T = []

for _ in range(V):
    x, y, t = map(int, input().split())
    T.append((x - 1, y - 1, t))

# 화산쇄설류가 덥쳐지는 시간을 미리 구함
cover_pyroclast_times = [[float("inf") for _ in range(N)] for _ in range(M)]

for u in range(M):
    for v in range(N):
        for x, y, t in T:
            cover_pyroclast_time = t + abs(u - x) + abs(v - y)

            # 가장 빨리 도달하는 화산쇄설류 시간을 적용
            cover_pyroclast_times[u][v] = min(cover_pyroclast_times[u][v], cover_pyroclast_time)

print(*bfs())
