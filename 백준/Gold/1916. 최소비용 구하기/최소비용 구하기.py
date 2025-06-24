import sys, heapq

input = sys.stdin.readline


# 다익스트라
def dijkstra(graph, start, dest):
    # 노드 간 비용
    costs = {node: float("inf") for node in range(1, n + 1)}
    costs[start] = 0

    # 방문한 노드
    queue = []
    heapq.heappush(queue, (start, 0))  # start 노드부터 방문 시작

    while queue:
        curr_node, curr_cost = heapq.heappop(queue)

        # 현재 노드의 비용이 기존의 비용보다 크면 패스(갱신할 필요 없음)
        if costs[curr_node] < curr_cost:
            continue

        # 현재 노드에서 방문할 노드와 그 노드까지의 비용
        for dest_node, new_cost in graph[curr_node]:
            cost = curr_cost + new_cost

            # 방문할 노드의 비용이 지금보다 더 크면 갱신
            if costs[dest_node] > cost:
                costs[dest_node] = cost
                heapq.heappush(queue, (dest_node, cost))

    return costs[dest]


# main
n = int(input())
m = int(input())

buses = {node: [] for node in range(1, n + 1)}

for _ in range(m):
    s, d, c = map(int, input().split())
    buses[s].append((d, c))

start, dest = map(int, input().split())

print(dijkstra(buses, start, dest))
