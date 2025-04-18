from collections import defaultdict, deque


def bfs(family, visited, p1, p2):
    queue = deque([(p1, 0)])
    visited.add(p1)

    while queue:
        curr_p, cnt = queue.popleft()

        if curr_p == p2:
            return cnt

        for adj_p in family[curr_p]:
            if adj_p not in visited:
                queue.append((adj_p, cnt + 1))
                visited.add(adj_p)

    return -1


# main
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

family = defaultdict(list)
visited = set()

for _ in range(m):
    u, v = map(int, input().split())  # 쌍방으로 노드 연결
    family[u].append(v)
    family[v].append(u)

print(bfs(family, visited, p1, p2))
