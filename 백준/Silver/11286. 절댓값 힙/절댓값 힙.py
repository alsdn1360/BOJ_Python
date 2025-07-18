import heapq, sys

input = sys.stdin.readline

# main
n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
            continue

        print(heapq.heappop(heap)[1])
