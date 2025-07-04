import heapq, sys

input = sys.stdin.readline


def dijkstra(road, start):
    times = {node: float("inf") for node in range(1, n + 1)}
    times[start] = 0

    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        curr_node, curr_time = heapq.heappop(queue)

        if times[curr_node] < curr_time:
            continue

        for dest_node, new_time in road[curr_node]:
            time = curr_time + new_time

            if times[dest_node] > time:
                times[dest_node] = time
                heapq.heappush(queue, (dest_node, time))

    return times


# main
n, m, x = map(int, input().split())

basic_road = {node: [] for node in range(1, n + 1)}
reverse_road = {node: [] for node in range(1, n + 1)}

for _ in range(m):
    s, e, t = map(int, input().split())
    basic_road[s].append((e, t))
    reverse_road[e].append((s, t))

# 원래 방향의 그래프에서 start가 x면, x에서 각 집으로 가는 시간을 뜻함(돌아가는 시간)
# 반대로 방향을 바꾼 그래프에서 start가 x면, 각 집에서 x로 가는 시간을 뜻함(x로 가는 시간)
time_to_x = dijkstra(reverse_road, x)  # 각 집에서 x로 가는 시간을 담고있음
time_from_x = dijkstra(basic_road, x)  # x에서 각 집으로 가는 시간을 담고있음

answer = 0

for i in range(1, n + 1):
    if i == x:
        continue

    answer = max(answer, time_to_x[i] + time_from_x[i])

print(answer)
