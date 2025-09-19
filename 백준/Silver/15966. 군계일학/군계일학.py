import sys

input = sys.stdin.readline

# main
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (max(a) + 1)

for i in a:
    dp[i] = dp[i - 1] + 1

print(max(dp))
