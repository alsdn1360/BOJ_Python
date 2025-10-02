import sys

input = sys.stdin.readline

EDIT_NUM = 100000000

# main
n = int(input())
lines = sorted([(x + EDIT_NUM, y + EDIT_NUM) for x, y in (map(int, input().split()) for _ in range(n))])

l, r = lines[0][0], lines[0][1]

ans = 0

for x, y in lines[1:]:
    if r <= x:
        ans += r - l
        l = x

    r = max(r, y)

ans += r - l

print(ans)
