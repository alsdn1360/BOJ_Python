import sys, heapq

input = sys.stdin.readline

# main
n, m = map(int, input().split())
a = list(map(int, input().split()))

heapq.heapify(a)

for _ in range(m):
    x = heapq.heappop(a)
    y = heapq.heappop(a)

    temp = x + y

    heapq.heappush(a, temp)
    heapq.heappush(a, temp)

print(sum(a))
