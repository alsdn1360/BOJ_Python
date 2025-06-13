# main
T = int(input())

dp = [0] * 10001
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 10001):
    # 1로 n을 만드는 경우 -> 1개
    # 1, 2로 n을 만드는 경우 -> (n / 2)개
    # 1, 2, 3 전부 사용해서 n을 만드는 경우-> dp[n - 3]개
    dp[i] = 1 + (i // 2) + dp[i - 3]

for _ in range(T):
    n = int(input())

    print(dp[n])
