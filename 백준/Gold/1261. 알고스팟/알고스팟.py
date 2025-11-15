from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs():
    queue = deque([(0, 0, 0)])  # x, y, 부순 벽의 갯수

    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == (N - 1, M - 1):
            return cnt

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny]:
                if maze[nx][ny] == 0:
                    queue.appendleft((nx, ny, cnt))  # 비용이 더 적은 것을 먼저 탐색할 수 있도록 왼쪽에 넣어줌
                else:
                    queue.append((nx, ny, cnt + 1))

                visited[nx][ny] = True


# main
M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())
