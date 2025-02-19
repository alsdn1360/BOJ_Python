from collections import deque

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, paper, n, m):
    queue = deque([(i, j)])
    paper[i][j] = 0
    area = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                queue.append((nx, ny))
                paper[nx][ny] = 0
                area += 1

    return area


# main
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
pic_cnt = 0
answer = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            pic_cnt += 1
            answer = max(answer, bfs(i, j, paper, n, m))

print(pic_cnt)
print(answer)
