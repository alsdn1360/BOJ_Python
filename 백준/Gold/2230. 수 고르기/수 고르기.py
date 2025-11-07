import sys

input = sys.stdin.readline

# main
n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

min_diff = float("inf")

l, r = 0, 1

while r < n and l <= r:
    diff = abs(a[r] - a[l])

    if diff < m:
        r += 1
    else:
        if diff < min_diff:
            min_diff = diff

        l += 1

print(min_diff)