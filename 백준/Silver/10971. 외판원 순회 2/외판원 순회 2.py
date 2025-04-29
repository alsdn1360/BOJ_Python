def dfs(curr_city, visited_cnt, cost):
    if visited_cnt == n and w[curr_city][0] != 0:
        return cost + w[curr_city][0]

    min_cost = float("inf")

    for adj_city in range(n):
        adj_cost = w[curr_city][adj_city]

        if adj_cost != 0 and not visited[adj_city]:
            visited[adj_city] = True

            min_cost = min(min_cost, dfs(adj_city, visited_cnt + 1, cost + adj_cost))

            visited[adj_city] = False

    return min_cost


# main
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
visited[0] = True

print(dfs(0, 1, 0))
