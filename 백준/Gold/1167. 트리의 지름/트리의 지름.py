import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    dists = [float("inf")] * (v + 1)
    dists[0], dists[start] = -1, 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if dists[curr_node] < curr_dist:
            continue

        for next_node, next_dist in tree[curr_node]:
            dist = curr_dist + next_dist

            if dists[next_node] > dist:
                dists[next_node] = dist
                heapq.heappush(queue, (dist, next_node))

    return dists


# main
v = int(input())
tree = {node: [] for node in range(1, v + 1)}

for _ in range(v):
    edges = list(map(int, input().split()))

    curr_node = edges[0]

    for i in range(1, len(edges) - 2, 2):
        adj_node = edges[i]
        dist = edges[i + 1]
        tree[curr_node].append((adj_node, dist))

dists_from_random = dijkstra(1)
fartest_node = dists_from_random.index(max(dists_from_random))
dists_froom_fartest_node = dijkstra(fartest_node)

print(max(dists_froom_fartest_node))
