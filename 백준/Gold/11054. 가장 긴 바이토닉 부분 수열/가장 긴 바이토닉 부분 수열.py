# main
n = int(input())
a = list(map(int, input().split()))

dp_increase = [1] * n
dp_decrease = [1] * n

# LIS 구하기
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

# LDS 구하기
a_rev = list(reversed(a))

for i in range(1, n):
    for j in range(i):
        if a_rev[i] > a_rev[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

dp_decrease.reverse()  # dp_decrease는 뒤집은 a로 만든 것이기 때문에 이것도 뒤집어야 LDS가 됨

answer = []

for i in range(n):
    answer.append(dp_increase[i] + dp_decrease[i] - 1)

print(max(answer))
