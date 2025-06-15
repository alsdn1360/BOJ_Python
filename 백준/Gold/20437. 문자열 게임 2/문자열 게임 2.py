import sys
from collections import defaultdict

input = sys.stdin.readline

# main
T = int(input())

for _ in range(T):
    w = input().rstrip()
    k = int(input())

    w_dict = defaultdict(list)
    found = False

    for i, c in enumerate(w):
        w_dict[c].append(i)

    min_length = float("inf")
    max_length = 0

    for w_idx in w_dict.values():
        n = len(w_idx)

        # 알파벳의 개수가 k보다 적으면 답이 될 수 없음
        if n < k:
            continue

        for i in range(n - k + 1):
            length = w_idx[i + k - 1] - w_idx[i] + 1

            min_length = min(min_length, length)
            max_length = max(max_length, length)

            found = True

    print(min_length, max_length) if found else print(-1)
