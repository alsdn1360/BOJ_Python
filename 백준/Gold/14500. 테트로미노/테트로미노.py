import sys

input = sys.stdin.readline

MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


# DFS로 'ㅗ' 모양을 제외한 테트로미노 탐색
def dfs(x, y, depth, curr_sum):
    global answer

    if depth == 4:
        answer = max(answer, curr_sum)
        return

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True

            dfs(nx, ny, depth + 1, curr_sum + paper[nx][ny])

            visited[nx][ny] = False


# 'ㅗ' 모양 테트로미노를 별도로 탐색하는 함수
def check_T_shape(x, y):
    global answer
    # 현재 위치(x, y)를 중심 블록으로 간주하고,
    # 주변 4방향(상,하,좌,우) 중 3개를 선택하는 모든 경우를 확인
    for i in range(4):
        temp_sum = paper[x][y]

        # 4방향 중 3방향을 선택하는 조합을 만듦
        # (i+0)%4, (i+1)%4, (i+2)%4 와 같이 3개의 날개를 선택
        for j in range(3):
            k = (i + j) % 4
            nx, ny = x + MOVES[k][0], y + MOVES[k][1]

            # 날개 하나라도 범위를 벗어나면 이 모양은 만들 수 없음
            if not in_bound(nx, ny):
                temp_sum = 0
                break

            temp_sum += paper[nx][ny]

        answer = max(answer, temp_sum)


# main
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

answer = 0
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = True

        dfs(i, j, 1, paper[i][j])

        visited[i][j] = False

        check_T_shape(i, j)

print(answer)
