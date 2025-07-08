import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    dists = [float("inf")] * (n + 1)
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
n = int(input())

tree = {node: [] for node in range(1, n + 1)}

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

dists = dijkstra(1)
fartest_node = dists.index(max(dists))
dists_froom_fartest_node = dijkstra(fartest_node)

print(max(dists_froom_fartest_node))
