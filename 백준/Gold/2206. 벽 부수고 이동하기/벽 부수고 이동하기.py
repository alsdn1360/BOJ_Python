from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs():
    queue = deque([(0, 0, 0)])  # x, y, 벽 부쉈는지 여부(0: 안부숨, 1: 부숨)

    # visited[x][y][0]: 벽을 안부수고 온 최단 거리
    # visited[x][y][1]: 벽을 부수고 온 최단 거리
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while queue:
        x, y, broken_state = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][broken_state]

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny):
                if maps[nx][ny] == 0 and visited[nx][ny][broken_state] == 0:
                    queue.append((nx, ny, broken_state))
                    visited[nx][ny][broken_state] = visited[x][y][broken_state] + 1
                elif maps[nx][ny] == 1 and broken_state == 0 and visited[nx][ny][1] == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][broken_state] + 1

    return -1


# main
n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())
