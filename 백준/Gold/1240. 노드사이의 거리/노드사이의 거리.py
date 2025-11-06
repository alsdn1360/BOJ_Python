from collections import deque


def bfs(graph, start, end):
    queue = deque([(start, 0)])

    visited = set()
    visited.add(start)

    while queue:
        curr_node, curr_cost = queue.popleft()

        if curr_node == end:
            return curr_cost

        for adj_node, cost_to_adj_node in graph[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, curr_cost + cost_to_adj_node))
                visited.add(adj_node)

    return


# main
n, m = map(int, input().split())

graph = {node: [] for node in range(1, n + 1)}

for _ in range(n - 1):
    u, v, c = map(int, input().split())

    graph[u].append((v, c))
    graph[v].append((u, c))

for _ in range(m):
    u, v = map(int, input().split())

    print(bfs(graph, u, v))
