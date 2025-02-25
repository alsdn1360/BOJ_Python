import sys
from collections import defaultdict, deque


def bfs(adj_list, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        curr_node = queue.popleft()

        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append(adj_node)
                visited.add(adj_node)


# main
N, M = map(int, sys.stdin.readline().split())

adj_list = defaultdict(list)
visited = set()
cc = 0

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())

    adj_list[u].append(v)
    adj_list[v].append(u)

for curr_node in range(1, N + 1):
    if curr_node not in visited:
        bfs(adj_list, curr_node, visited)
        cc += 1

print(cc)
