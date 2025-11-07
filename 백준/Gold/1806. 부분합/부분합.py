import sys

input = sys.stdin.readline

# main
n, s = map(int, input().split())
a = list(map(int, input().split()))

if a[0] >= s:
    print(1)
    sys.exit()

prefix_sum = [0] * (n + 1)
prefix_sum[1] = a[0]

for i in range(2, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

l, r = 0, 1
min_len = float("inf")

while r < n + 1 and l <= r:
    seq_sum = prefix_sum[r] - prefix_sum[l]

    if seq_sum < s:
        r += 1
    else:
        min_len = min(min_len, r - l)
        l += 1

print(min_len) if min_len != float("inf") else print(0)
