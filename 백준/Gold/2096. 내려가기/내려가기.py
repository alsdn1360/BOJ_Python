import sys

input = sys.stdin.readline

# main
n = int(input())

a, b, c = map(int, input().split())

max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    # 최대 점수
    max_a, max_b, max_c = max_dp[0], max_dp[1], max_dp[2]

    max_dp[0] = a + max(max_a, max_b)
    max_dp[1] = b + max(max_a, max_b, max_c)
    max_dp[2] = c + max(max_b, max_c)

    # 최소 점수
    min_a, min_b, min_c = min_dp[0], min_dp[1], min_dp[2]

    min_dp[0] = a + min(min_a, min_b)
    min_dp[1] = b + min(min_a, min_b, min_c)
    min_dp[2] = c + min(min_b, min_c)


print(f"{max(max_dp)} {min(min_dp)}")
