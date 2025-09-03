# main
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]  # dp[자릿수][가장 마지막에 오는 숫자의 개수]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n + 1):
    dp[i][0] += dp[i - 1][1] % 1000000000  # 마지막 숫자가 0일 때는 1만 올 수 있음
    dp[i][9] += dp[i - 1][8] % 1000000000  # 마지막 숫자가 9일 때는 8만 올 수 있음

    for j in range(1, 9):  # 마지막 숫자가 1 ~ 8이면 각각 +1, -1이 올 수 있음
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000

print(sum(dp[n]) % 1000000000)
