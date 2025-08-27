from collections import deque
import sys

input = sys.stdin.readline


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < n


# main
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

# 1. 처음 상어 위치 파악
shark = None
shark_size = 2

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark = (i, j)

# 2. 물고기 먹으러 가기
time = 0
eaten_fish = 0

while True:
    fishes = deque()

    queue = deque([(shark[0], shark[1], 0)])

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[shark[0]][shark[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny] and sea[nx][ny] <= shark_size:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True

                if 0 < sea[nx][ny] < shark_size:
                    fishes.append((nx, ny, sea[nx][ny], dist + 1))

    fishes = deque(sorted(fishes, key=lambda x: (x[3], x[0], x[1])))

    if not fishes:
        break

    fx, fy, fish_size, dist = fishes.popleft()

    # 물고기 먹기
    if shark_size > fish_size:
        time += dist
        eaten_fish += 1
        sea[shark[0]][shark[1]] = 0  # 원래있던 칸은 0으로 만들기

        shark = (fx, fy)
        sea[fx][fy] = 9  # 물고기를 먹기 위해서 간 자리를 9로 만듦

    # 상어 진화
    if eaten_fish == shark_size:
        shark_size += 1
        eaten_fish = 0

print(time)
