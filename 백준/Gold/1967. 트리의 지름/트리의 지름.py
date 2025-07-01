import sys, heapq

input = sys.stdin.readline


def dijkstra(tree, start):
    costs = {i: float("inf") for i in range(1, n + 1)}
    costs[start] = 0

    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        curr_node, curr_cost = heapq.heappop(queue)

        if costs[curr_node] < curr_cost:
            continue

        for dest_node, new_cost in tree[curr_node]:
            cost = curr_cost + new_cost

            if costs[dest_node] > cost:
                costs[dest_node] = cost
                heapq.heappush(queue, (dest_node, cost))

    return costs


# main
n = int(input())

tree = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

# 루트로 부터 모든 노드까지의 거리
costs_from_root = dijkstra(tree, 1)

# 그 중에서 가장 먼 노드
fartest_node = max(costs_from_root, key=costs_from_root.get)

# 가장 먼 노드에서 모든 노드까지의 거리
costs_from_fartest_node = dijkstra(tree, fartest_node)

print(max(costs_from_fartest_node.values()))
