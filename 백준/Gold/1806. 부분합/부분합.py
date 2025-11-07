import sys

input = sys.stdin.readline

# main
n, s = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 0
min_len = float("inf")
curr_sum = 0

while True:
    if curr_sum >= s:
        min_len = min(min_len, r - l)
        curr_sum -= a[l]
        l += 1
    elif r == n:
        break
    else:
        curr_sum += a[r]
        r += 1

print(min_len) if min_len != float("inf") else print(0)
