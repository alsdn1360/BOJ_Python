import sys

input = sys.stdin.readline


# main
n, k = map(int, input().split())
a = list(map(int, input().split()))

moved_cnt = 0
min_key = a[0]
max_key = a[0]

for i in range(1, n):
    min_key = min(min_key, a[i])
    max_key = max(max_key, a[i])

    # 최댒값이 범위를 넘어서면 손 위치를 옮겨야 함
    if max_key - min_key >= k:
        moved_cnt += 1
        min_key = a[i]
        max_key = a[i]

print(moved_cnt)
