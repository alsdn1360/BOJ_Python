import sys

input = sys.stdin.readline


# MST 구현
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])

    return parents[x]


def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if rank[xroot] > rank[yroot]:
        parents[yroot] = xroot
    elif rank[yroot] > rank[xroot]:
        parents[xroot] = yroot
    else:
        parents[xroot] = yroot
        rank[yroot] += 1


# main
n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

# 연결되어 있는 지사 컴퓨터들을 묶어줌
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

costs = [list(map(int, input().split())) for _ in range(n)]

edges = []

# 본사 컴퓨터인 1번 컴퓨터는 모든 지사의 네트워크 컴퓨터와 연결되어있으므로 볼 필요 없음
for i in range(1, n):
    for j in range(i + 1, n):
        cost, x, y = costs[i][j], i + 1, j + 1

        if cost == 0:
            continue

        edges.append((cost, x, y))

edges.sort()

total_cost = 0
new_edges = []

for cost, x, y in edges:
    # 루트가 다르면 연결되어 있지 않기 때문에 연결해줘야 함
    if find(x) != find(y):
        union(x, y)
        total_cost += cost
        new_edges.append((x, y))

print(total_cost, len(new_edges))

if new_edges:
    for x, y in new_edges:
        print(x, y)
