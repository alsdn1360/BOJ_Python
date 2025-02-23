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
    elif rank[xroot] < rank[yroot]:
        tree[xroot] = yroot
    else:
        tree[xroot] = yroot
        rank[yroot] += 1

# main
N = int(input())
M = int(input())

costs = [list(map(int, input().split())) for _ in range(M)]
costs.sort(key = lambda x : x[2])

tree = [i for i in range(N)]
rank = [0] * N

min_cost = 0
edges = 0

for edge in costs:
    if edges == N - 1:
        break

    x = find(tree, edge[0] - 1)
    y = find(tree, edge[1] - 1)

    if x != y:
        union(tree, rank, x, y)
        min_cost += edge[2]
        edges += 1

print(min_cost)