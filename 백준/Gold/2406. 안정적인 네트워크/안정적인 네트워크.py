import sys

input = sys.stdin.readline


def find(tree, x):
    if tree[x] == x:
        return x

    tree[x] = find(tree, tree[x])

    return tree[x]


def union(tree, rank, x, y):
    xroot = find(tree, x)
    yroot = find(tree, y)

    if rank[xroot] > rank[yroot]:
        tree[yroot] = xroot
    elif rank[yroot] > rank[xroot]:
        tree[xroot] = yroot
    else:
        tree[xroot] = yroot
        rank[yroot] += 1


# main
n, m = map(int, input().split())

computers = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    union(computers, rank, x, y)

costs = [list(map(int, input().split())) for _ in range(n)]

networks = []

for i in range(1, n):
    for j in range(1, n):
        if costs[i][j] == 0:
            continue

        networks.append((costs[i][j], i + 1, j + 1))

networks.sort()

total_cost = 0
new_networks = []

for cost, x, y in networks:
    # 루트가 다르면 연결되어 있지 않기 때문에 연결해줘야 함
    if find(computers, x) != find(computers, y):
        union(computers, rank, x, y)
        total_cost += cost
        new_networks.append((x, y))

print(total_cost, len(new_networks))

if new_networks:
    for x, y in new_networks:
        print(x, y)
