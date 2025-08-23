import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    dists = [float("inf") for _ in range(n + 1)]
    dists[0], dists[start] = -1, 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        curr_dist, curr_area = heapq.heappop(queue)

        # 지금 거리가 더 크면 갱신할 필요가 없음(이미 더 크니까)
        if dists[curr_area] < curr_dist:
            continue

        for adj_area, adj_dist in field[curr_area]:
            dist = curr_dist + adj_dist

            # 원래의 거리가 더 크면 갱신해야 함(더 작은 거리니까)
            if dists[adj_area] > dist:
                dists[adj_area] = dist
                heapq.heappush(queue, (dist, adj_area))

    total_items = 0

    for i in range(1, n + 1):
        if dists[i] <= m:
            total_items += items[i - 1]

    return total_items


# main
n, m, r = map(int, input().split())
items = list(map(int, input().split()))

field = {area: [] for area in range(1, n + 1)}

for _ in range(r):
    a, b, l = map(int, input().split())

    field[a].append((b, l))
    field[b].append((a, l))

ans = 0

for area in range(1, n + 1):
    ans = max(ans, dijkstra(area))

print(ans)
