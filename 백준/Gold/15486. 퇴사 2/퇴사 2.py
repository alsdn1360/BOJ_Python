import sys

input = sys.stdin.readline

# main
n = int(input())

t = []
p = []

for _ in range(n):
    ti, pi = map(int, input().split())

    t.append(ti)
    p.append(pi)

dp = [0] * (n + 1)

for day in range(n - 1, -1, -1):
    if day + t[day] > n:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], dp[day + t[day]] + p[day])

print(dp[0])
