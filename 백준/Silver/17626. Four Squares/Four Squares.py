import math

# main
n = int(input())

dp = [float("inf")] * (n + 1)

for i in range(1, n + 1):
    # i가 제곱수면 최소는 1
    if math.sqrt(i) % 1 == 0:
        dp[i] = 1
    # i보다 작은 제곱수를 뺐을 때, 최소값
    else:
        for j in range(1, math.floor(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[n])
