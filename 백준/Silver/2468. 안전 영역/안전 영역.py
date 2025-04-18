from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def oob(n, nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def bfs(n, area, visited, i, j, rain_h):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if oob(n, nx, ny) and area[nx][ny] > rain_h and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


# main
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

max_rain_h = 0
safe_area = 0

# 높이가 가장 높은 비의 높이 구하기
for i in range(n):
    max_rain_h = max(max_rain_h, max(area[i]))

# 비가 전혀 내리지 않았을 때도 고려해서 0부터 시작
for curr_rain_h in range(0, max_rain_h + 1):
    # 현재 비의 높이 마다 새롭게 초기화해야 함
    curr_visited = [[False for _ in range(n)] for _ in range(n)]
    curr_safe_area = 0

    for i in range(n):
        for j in range(n):
            if area[i][j] > curr_rain_h and not curr_visited[i][j]:
                bfs(n, area, curr_visited, i, j, curr_rain_h)
                curr_safe_area += 1

    safe_area = max(safe_area, curr_safe_area)

print(safe_area)
