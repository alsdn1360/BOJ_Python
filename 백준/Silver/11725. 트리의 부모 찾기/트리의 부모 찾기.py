import sys
from collections import defaultdict, deque


input = sys.stdin.readline


def bfs():
    queue = deque([1])

    visited = [False] * (n + 1)
    visited[1] = True

    while queue:
        curr_n = queue.popleft()

        for adj_n in tree[curr_n]:
            if not visited[adj_n]:
                queue.append(adj_n)
                visited[adj_n] = True
            else:
                answer[curr_n] = adj_n


# main
n = int(input())

tree = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

answer = [0] * (n + 1)

bfs()

for i in range(2, n + 1):
    print(answer[i])
