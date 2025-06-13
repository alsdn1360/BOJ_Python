# main
T = int(input())

dp = [0] * 10001
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 10001):
    # 1과 2로만 n을 만드는 경우는 특정 규칙이 있음 -> n / 2 + 1
    # 어떤 조합이든 3을 뺀 n - 3을 만드는 조합이 됨 -> dp[n - 3]
    dp[i] = (i // 2 + 1) + dp[i - 3]

for _ in range(T):
    n = int(input())

    print(dp[n])
