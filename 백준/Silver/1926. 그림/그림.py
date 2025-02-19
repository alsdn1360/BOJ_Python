from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    paper[i][j] = 0

    area = 1
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                queue.append((nx, ny))
                paper[nx][ny] = 0
                area += 1

    return area


# main
n, m = map(int, input().split())
pic_cnt = 0
answer = 0

paper = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            pic_cnt += 1
            answer = max(answer, bfs(i, j))

print(pic_cnt)
print(answer)
