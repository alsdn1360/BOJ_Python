import sys, heapq

input = sys.stdin.readline


def dijkstra(start, end):
    costs = {city: float("inf") for city in range(1, n + 1)}
    costs[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    prev_cities = {city: 0 for city in range(1, n + 1)}

    while queue:
        curr_cost, curr_city = heapq.heappop(queue)

        if costs[curr_city] < curr_cost:
            continue

        for nxt_city, nxt_cost in buses[curr_city]:
            total_cost = curr_cost + nxt_cost

            if costs[nxt_city] > total_cost:
                costs[nxt_city] = total_cost
                heapq.heappush(queue, (total_cost, nxt_city))
                prev_cities[nxt_city] = curr_city

    return costs[end], prev_cities


# main
n = int(input())
m = int(input())

buses = {city: [] for city in range(1, n + 1)}

for _ in range(m):
    s, e, c = map(int, input().split())

    buses[s].append((e, c))

start, end = map(int, input().split())

# 최소 비용 구하기
min_cost, prev_cities = dijkstra(start, end)

# 경로 구하기
prev_city = end
path = [prev_city]

while True:
    prev_city = prev_cities[prev_city]
    
    path.append(prev_city)

    if prev_city == start:
        break

print(min_cost)
print(len(path))
print(*list(reversed(path)))
