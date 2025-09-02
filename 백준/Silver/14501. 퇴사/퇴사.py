# main
n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    today_t = works[i][0]
    today_p = works[i][1]

    if i + today_t > n:
        dp[i] = dp[i + 1]  # 오늘 일 못할 때
    else:
        dp[i] = max(dp[i + 1], dp[i + today_t] + today_p)  # 오늘 일 안할 때 vs 오늘 일 할 때

print(dp[0])
