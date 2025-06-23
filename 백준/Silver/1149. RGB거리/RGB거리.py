# main
n = int(input())

# 빨강, 초록, 파랑
dp = [0, 0, 0]

for _ in range(n):
    r, g, b = map(int, input().split())

    prev_r, prev_g, prev_b = dp[0], dp[1], dp[2]

    dp[0] = r + min(prev_g, prev_b)
    dp[1] = g + min(prev_r, prev_b)
    dp[2] = b + min(prev_r, prev_g)

print(min(dp))
