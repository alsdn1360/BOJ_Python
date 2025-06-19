# main
n = int(input())

answer = 0
times = []

for _ in range(n):
    start, end = map(int, input().split())

    times.append((start, end))

# 회의가 가장 빨리 끝나는 순으로 정렬
times.sort(key=lambda x: (x[1], x[0]))

prev_end = 0

for time in times:
    curr_start = time[0]

    if curr_start >= prev_end:
        answer += 1
        prev_end = time[1]

print(answer)
