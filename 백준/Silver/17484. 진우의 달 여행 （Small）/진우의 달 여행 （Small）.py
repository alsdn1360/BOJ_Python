# main
n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

dp = [[[float("inf") for _ in range(3)] for _ in range(m)] for _ in range(n)]

# dp 첫 행 초기화 -> 어느 방향에서나 접근 가능
for j in range(m):
    for d in range(3):
        dp[0][j][d] = space[0][j]

for i in range(1, n):
    for j in range(m):
        if j > 0:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + space[i][j]

        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + space[i][j]

        if j < m - 1:
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + space[i][j]

answer = float("inf")

# 세 방향에서 최솟값 찾기
for j in range(m):
    for d in range(3):
        answer = min(answer, dp[n - 1][j][d])

print(answer)
