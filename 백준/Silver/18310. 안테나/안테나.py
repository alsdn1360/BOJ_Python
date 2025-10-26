import sys

input = sys.stdin.readline

# main
n = int(input())
hs = sorted(list(map(int, input().split())))

ans = 0

if n % 2 == 0:
    ans = hs[n // 2 - 1]
else:
    ans = hs[n // 2]

print(ans)
