import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    dists = {node: float("inf") for node in range(1, v + 1)}
    dists[start] = 0

    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        curr_node, curr_dist = heapq.heappop(queue)

        if dists[curr_node] < curr_dist:
            continue

        for next_node, next_dist in tree[curr_node]:
            dist = curr_dist + next_dist
            if dists[next_node] > dist:
                dists[next_node] = dist
                heapq.heappush(queue, (next_node, dist))

    return dists


# main
v = int(input())
tree = {node: [] for node in range(1, v + 1)}

for _ in range(v):
    edges = list(map(int, input().split()))

    ends = []
    dists = []

    for i in range(1, len(edges) - 1):
        if i % 2 != 0:
            ends.append(edges[i])
        else:
            dists.append(edges[i])

    for i in range(len(ends)):
        tree[edges[0]].append((ends[i], dists[i]))
        tree[ends[i]].append((edges[0], dists[i]))

# 루트로 부터 모든 노드까지의 거리
costs_from_root = dijkstra(1)

# 그 중에서 가장 먼 노드
fartest_node = max(costs_from_root, key=costs_from_root.get)

# 가장 먼 노드에서 모든 노드까지의 거리
costs_from_fartest_node = dijkstra(fartest_node)

print(max(costs_from_fartest_node.values()))
