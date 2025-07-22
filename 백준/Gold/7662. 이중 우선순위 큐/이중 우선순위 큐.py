from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

# main
t = int(input())

for _ in range(t):
    k = int(input())

    q = defaultdict(int)
    max_q = []
    min_q = []

    for _ in range(k):
        o, n = input().split()
        n = int(n)

        if o == "I":
            q[n] += 1
            heapq.heappush(max_q, (-n, n))
            heapq.heappush(min_q, n)
        else:
            if not max_q or not min_q:
                continue

            if n > 0:
                while max_q:
                    max_n = heapq.heappop(max_q)[1]

                    if q[max_n] > 0:
                        q[max_n] -= 1
                        break
            else:
                while min_q:
                    min_n = heapq.heappop(min_q)

                    if q[min_n] > 0:
                        q[min_n] -= 1
                        break

    q = [k for k, v in q.items() if v > 0]

    if q:
        print(max(q), min(q))
    else:
        print("EMPTY")
