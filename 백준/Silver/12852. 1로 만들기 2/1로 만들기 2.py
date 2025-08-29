# main
n = int(input())

cnt_dp = [0] * (n + 1)  # 연산 횟수(할 수 있는 연산을 반대로 할거임)

for i in range(2, n + 1):
    # 3. 1을 뺀다
    cnt_dp[i] = cnt_dp[i - 1] + 1

    # 2. X가 2로 나누어 떨어지면, 2로 나눈다
    if i % 2 == 0:
        cnt_dp[i] = min(cnt_dp[i], cnt_dp[i // 2] + 1)

    # 1. X가 3으로 나누어 떨어지면, 3으로 나눈다
    if i % 3 == 0:
        cnt_dp[i] = min(cnt_dp[i], cnt_dp[i // 3] + 1)

num_dp = []  # 방법에 포함되어 있는 수
curr_n = n

# 방법은 역추적을 이용
# 이전 숫자는 반드시 curr_n // 3, curr_n // 2, curr_n - 1 중에서 골라야 함
while curr_n > 0:
    num_dp.append(curr_n)

    if curr_n % 3 == 0:
        if cnt_dp[curr_n // 3] == cnt_dp[curr_n] - 1:
            curr_n = curr_n // 3
            continue

    if curr_n % 2 == 0:
        if cnt_dp[curr_n // 2] == cnt_dp[curr_n] - 1:
            curr_n = curr_n // 2
            continue

    curr_n -= 1

print(cnt_dp[n])
print(*num_dp)
