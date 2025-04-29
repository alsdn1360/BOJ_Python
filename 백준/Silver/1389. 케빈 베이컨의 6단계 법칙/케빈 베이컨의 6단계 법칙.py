from collections import defaultdict, deque


def bfs(start_user):
    queue = deque([start_user])

    dist = [-1] * (n + 1)
    dist[start_user] = 0

    while queue:
        curr_user = queue.popleft()

        for adj_user in friends[curr_user]:
            if dist[adj_user] == -1:
                queue.append(adj_user)

                dist[adj_user] = dist[curr_user] + 1

    return sum(dist[1:])


# main
n, m = map(int, input().split())

friends = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())

    friends[a].append(b)
    friends[b].append(a)

bacon = []

for user in range(1, n + 1):
    dist_per_user = bfs(user)
    bacon.append((user, dist_per_user))

bacon.sort(key=lambda x: (x[1], x[0]))

print(bacon[0][0])
