from collections import deque


def bfs(end):
    queue = deque()
    queue.append((0, 0, 1))
    maze[0][0] = 0

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y, steps = queue.popleft()

        if x == end[0] and y == end[1]:
            return steps

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny, steps + 1))
                maze[nx][ny] = 0


# main
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs((n - 1, m - 1)))
