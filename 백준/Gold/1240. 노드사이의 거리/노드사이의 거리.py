import heapq


def dijkstra(graph, start, end):
    costs = {node: float("inf") for node in range(1, n + 1)}
    costs[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        if curr_cost < costs[curr_node]:
            continue

        for cost_to_adj_node, adj_node in graph[curr_node]:
            cost = curr_cost + cost_to_adj_node

            if cost < costs[adj_node]:
                costs[adj_node] = cost
                heapq.heappush(queue, (cost, adj_node))

    return costs[end]


# main
n, m = map(int, input().split())

graph = {node: [] for node in range(1, n + 1)}

for _ in range(n - 1):
    u, v, c = map(int, input().split())

    graph[u].append((c, v))
    graph[v].append((c, u))

for _ in range(m):
    u, v = map(int, input().split())

    print(dijkstra(graph, u, v))
