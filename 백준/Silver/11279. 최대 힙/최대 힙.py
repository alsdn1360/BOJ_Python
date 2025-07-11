import heapq, sys

input = sys.stdin.readline

# main
n = int(input())

max_heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if max_heap:
            print(abs(heapq.heappop(max_heap)))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -x)
