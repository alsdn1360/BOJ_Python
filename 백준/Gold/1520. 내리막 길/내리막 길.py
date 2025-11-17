import heapq

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < M and 0 <= ny < N


def bfs():
    queue = []
    heapq.heappush(queue, (-grid[0][0], 0, 0))

    while queue:
        curr_h, x, y = heapq.heappop(queue)
        curr_h *= -1

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny):
                new_h = grid[nx][ny]

                if curr_h > new_h:
                    if dp[nx][ny] == 0:
                        heapq.heappush(queue, (-grid[nx][ny], nx, ny))

                    dp[nx][ny] += dp[x][y]

    return dp[M - 1][N - 1]


# main
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1

print(bfs())
