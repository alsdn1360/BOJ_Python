from collections import defaultdict, deque


def dfs(adj_list, curr_node, visited, answer):
    visited.add(curr_node)
    answer.append(curr_node)

    for adj_node in adj_list.get(curr_node, []):
        if adj_node not in visited:
            dfs(adj_list, adj_node, visited, answer)


def bfs(adj_list, start_node, visited, answer):
    queue = deque([start_node])
    visited.add(start_node)
    answer.append(start_node)

    while queue:
        curr_node = queue.popleft()

        for adj_node in adj_list.get(curr_node, []):
            if adj_node not in visited:
                queue.append(adj_node)
                visited.add(adj_node)
                answer.append(adj_node)


# main
N, M, V = map(int, input().split())

dfs_answer = []
dfs_visited = set()

bfs_answer = []
bfs_visited = set()

adj_list = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for key in adj_list:
    adj_list[key].sort()

dfs(adj_list, V, dfs_visited, dfs_answer)
bfs(adj_list, V, bfs_visited, bfs_answer)

print(*dfs_answer)
print(*bfs_answer)
