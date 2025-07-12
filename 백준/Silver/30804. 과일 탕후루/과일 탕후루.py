import sys
from collections import defaultdict

input = sys.stdin.readline

# main
n = int(input())
fruits = list(map(int, input().split()))

f_cnt = defaultdict(int)
left = 0
answer = 0

for right in range(n):
    f_cnt[fruits[right]] += 1

    while len(f_cnt) > 2:
        f_cnt[fruits[left]] -= 1

        if f_cnt[fruits[left]] == 0:
            del f_cnt[fruits[left]]

        left += 1

    answer = max(answer, right - left + 1)

print(answer)
