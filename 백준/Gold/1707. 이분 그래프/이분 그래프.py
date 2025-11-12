from collections import deque
import sys

input = sys.stdin.readline


def bfs(node):
    queue = deque([node])

    while queue:
        curr_node = queue.popleft()

        for adj_node in graph[curr_node]:
            if group[adj_node] == group[curr_node]:
                return False

            if group[adj_node] == 0:
                queue.append(adj_node)
                group[adj_node] = -group[curr_node]

    return True


# main
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = {node: [] for node in range(1, V + 1)}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    group = [0] * (V + 1)  # 그룹 번호 저장

    for node in range(1, V + 1):
        if group[node] != 0:
            continue

        group[node] = 1

        is_bi_graph = bfs(node)

        if not is_bi_graph:
            break

    print("YES") if is_bi_graph else print("NO")
