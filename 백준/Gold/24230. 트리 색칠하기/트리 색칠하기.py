from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def bfs():
    # 루트의 색이 하얀색이 아니면 일단 한 번 칠해줘야 함
    if colors[0] != 0:
        answer = 1
    else:
        answer = 0

    queue = deque([(1, colors[0])])
    visited = set()
    visited.add(1)

    while queue:
        parent_node, parent_color = queue.popleft()

        for adj_node in graph[parent_node]:
            if adj_node in visited:
                continue

            target_color = colors[adj_node - 1]

            if parent_color != target_color:
                answer += 1

            queue.append((adj_node, target_color))
            visited.add(adj_node)

    return answer


# main
n = int(input())
colors = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

print(bfs())
