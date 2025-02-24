from collections import defaultdict


def dfs(adj_list, curr_node, connect, visited):
    connect.append(curr_node)
    visited.add(curr_node)

    for adj_node in adj_list.get(curr_node, []):
        if adj_node not in visited:
            dfs(adj_list, adj_node, connect, visited)


# main
N = int(input())
V = int(input())

adj_list = defaultdict(list)
connect = []
visited = set()

for i in range(V):
    u, v = map(int, input().split())

    adj_list[u].append(v)
    adj_list[v].append(u)

dfs(adj_list, 1, connect, visited)

print(len(connect) - 1)
