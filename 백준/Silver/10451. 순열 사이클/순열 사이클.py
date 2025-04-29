from collections import defaultdict


def dfs(graph, visited, curr_node):
    visited.add(curr_node)

    for adj_node in graph[curr_node]:
        if adj_node not in visited:
            dfs(graph, visited, adj_node)


# main
t = int(input())

for i in range(t):
    answer = 0

    n = int(input())
    permu = list(map(int, input().split()))

    graph = defaultdict(list)
    visited = set()

    for i, elem in enumerate(permu):
        graph[i + 1].append(elem)

    for idx in range(1, n + 1):
        if idx not in visited:
            dfs(graph, visited, idx)
            answer += 1

    print(answer)
