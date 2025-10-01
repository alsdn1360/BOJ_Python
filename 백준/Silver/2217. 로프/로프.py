import sys

input = sys.stdin.readline

# main
n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0

for i in range(n):
    # ropes는 이미 내림차순 정렬이므로, ropes[i]는 항상 가장 작은 값을 가짐
    ans = max(ans, ropes[i] * (i + 1))

print(ans)
