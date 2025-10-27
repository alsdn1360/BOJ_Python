import sys

input = sys.stdin.readline

# main
n = int(input())
a = list(map(int, input().split()))

max_num = 0
increase_idx = []  # 증가하는 값들의 인덱스를 모아두는 리스트

for i, num in enumerate(a):
    if num >= max_num:
        max_num = num
        increase_idx.append(i)

increase_idx.append(n)

diffs = []  # 증가하는 값의 인덱스끼리의 거리들

for i in range(1, len(increase_idx)):
    diffs.append(increase_idx[i] - increase_idx[i - 1])

print(max(diffs))
