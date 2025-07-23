import sys, heapq

input = sys.stdin.readline


def dijkstra(start, target):
    costs = {node: float("inf") for node in range(1, n + 1)}
    costs[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if costs[curr_node] < curr_cost:
            continue

        for nxt_node, nxt_cost in graph[curr_node]:
            cost = curr_cost + nxt_cost

            if costs[nxt_node] > cost:
                costs[nxt_node] = cost
                heapq.heappush(heap, (cost, nxt_node))

    return costs[target]


# main
n, e = map(int, input().split())
graph = {node: [] for node in range(1, n + 1)}

for _ in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))

print(-1) if answer >= float("inf") else print(answer)
