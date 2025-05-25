from collections import Counter
import sys

input = sys.stdin.readline

# main
answer = []
voca = []

n, m = map(int, input().split())

for _ in range(n):
    word = input().rstrip()

    if len(word) >= m:
        voca.append(word)

voca_cnt = Counter(voca)

for v, v_c in voca_cnt.items():
    answer.append((v, v_c, len(v)))  # 단어, 단어 횟수, 단어 길이

answer.sort(key=lambda x: (-x[1], -x[2], x[0]))

for v, _, _ in answer:
    print(v)
