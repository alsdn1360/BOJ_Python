import sys

input = sys.stdin.readline

# main
n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 회의가 가장 빨리 끝나는 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

answer = 0
prev_end = 0

for start, end in meetings:
    if start >= prev_end:
        answer += 1
        prev_end = end

print(answer)
