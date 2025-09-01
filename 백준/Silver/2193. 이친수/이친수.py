# main
n = int(input())

dp = [[0, 0] for _ in range(n + 1)]

dp[1][0] = 0  # 0으로 끝나는 이친수의 개수
dp[1][1] = 1  # 1로 끝나는 이친수의 개수

for i in range(2, n + 1):
    # 0으로 끝나는 이친수의 뒤에는 0, 1 둘 다 가능
    dp[i][0] += dp[i - 1][0]
    dp[i][1] += dp[i - 1][0]

    # 1로 끝나는 이친수의 뒤에는 0만 가능
    dp[i][0] += dp[i - 1][1]

print(sum(dp[n]))
