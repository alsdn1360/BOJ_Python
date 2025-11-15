from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs():
    queue = deque([(0, 0)])  # x, y, 부순 벽의 갯수

    costs = [[float("inf") for _ in range(M)] for _ in range(N)]  # 0 혹은 1을 비용으로 생각함
    costs[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny):
                ncost = costs[x][y] + maze[x][y]  # 지금 위치와 새로운 위치에서의 비용을 구함

                if ncost < costs[nx][ny]:
                    costs[nx][ny] = ncost

                    if maze[nx][ny] == 0:
                        queue.appendleft((nx, ny))  # 비용이 0이면 앞에 넣어서 우선적으로 탐색하게 함
                    else:
                        queue.append((nx, ny))

    return costs[N - 1][M - 1]


# main
M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())
