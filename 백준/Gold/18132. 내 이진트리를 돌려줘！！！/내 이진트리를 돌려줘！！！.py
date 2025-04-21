MOD = 1000000007

# main
t = int(input())
edges = [int(input()) + 1 for _ in range(t)] # 노드의 개수는 간선보다 1 크므로 +1
max_e = max(edges)

dp = [0] * (max_e + 1)
dp[0] = dp[1] = 1

for i in range(2, max_e + 1):
    for j in range(i):
        dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD

for edge in edges:
    print(dp[edge])
