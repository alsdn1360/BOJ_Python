def in_bound(nr, nc):
    return 0 <= nr < n and 0 <= nc < n


def check_right_and_down(nr, nc):
    return in_bound(nr, nc) and house[nr][nc] != 1


def check_diagonal(nr, nc):
    return (
        in_bound(nr, nc)
        and house[nr - 1][nc] != 1
        and house[nr][nc - 1] != 1
        and house[nr][nc] != 1
    )


def dfs(state, r, c):
    if memo[r][c][state] != -1:
        return memo[r][c][state]

    if (r, c) == (n - 1, n - 1):
        return 1

    paths = 0

    # 가로 방향이면
    if state == 0:
        if check_right_and_down(r, c + 1):
            paths += dfs(0, r, c + 1)  # 가로로 이동

        if check_diagonal(r + 1, c + 1):
            paths += dfs(2, r + 1, c + 1)  # 대각선으로 이동
    # 세로 방향이면
    elif state == 1:
        if check_right_and_down(r + 1, c):
            paths += dfs(1, r + 1, c)  # 세로로 이동

        if check_diagonal(r + 1, c + 1):
            paths += dfs(2, r + 1, c + 1)  # 대각선으로 이동
    # 대각선 방향이면
    elif state == 2:
        if check_right_and_down(r, c + 1):
            paths += dfs(0, r, c + 1)  # 가로로 이동

        if check_right_and_down(r + 1, c):
            paths += dfs(1, r + 1, c)  # 세로로 이동

        if check_diagonal(r + 1, c + 1):
            paths += dfs(2, r + 1, c + 1)  # 대각선으로 이동

    memo[r][c][state] = paths

    return paths


# main
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
# 메모이제이션 사용(파이프 헤드 상태, 파이프 헤드 위치(r, c))
memo = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]

print(dfs(0, 0, 1))  # 현재 상태(가로), 파이프 헤드의 위치(0, 1)
