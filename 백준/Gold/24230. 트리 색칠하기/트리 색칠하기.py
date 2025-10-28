from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(parent_node, parent_color):
    global answer

    for adj_node in graph[parent_node]:
        if adj_node in visited:
            continue

        visited.add(adj_node)

        target_color = colors[adj_node - 1]

        if parent_color != target_color:
            answer += 1

        dfs(adj_node, colors[adj_node - 1])


# main
n = int(input())
colors = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# 루트의 색이 하얀색이 아니면 일단 한 번 칠해줘야 함
if colors[0] != 0:
    answer = 1
else:
    answer = 0

visited = set()
visited.add(1)

dfs(1, colors[0])

print(answer)
