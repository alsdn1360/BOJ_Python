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

costs = dijkstra(tree, 1)

# 루트에서 가장 멀리 있는 노드들
max_nodes = [u for u, v in costs.items() if v == max(costs.values())]

answer = 0

# 가장 먼 노드에서 또 가장 먼 노드 사이의 거리
for start in max_nodes:
    answer = max(answer, max(dijkstra(tree, start).values()))

print(answer)
