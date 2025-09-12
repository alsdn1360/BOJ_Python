import sys

input = sys.stdin.readline

# main
n = int(input())
x = list(map(int, input().split()))

x.sort()

ans = 0
idx = 0

while n > 0:
    # 현재 수용 가능한 팀 인원을 전체 인원 수에서 빼고, 그 다음 수용 가능한 팀 인원으로 이동
    n -= x[idx]
    idx += x[idx]

    ans += 1

print(ans)
