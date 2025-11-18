import sys

input = sys.stdin.readline


def find(tree, x):
    if tree[x] == x:
        return x

    tree[x] = find(tree, tree[x])

    return tree[x]


def union(rank, tree, x, y):
    x_root = find(tree, x)
    y_root = find(tree, y)

    if rank[x_root] < rank[y_root]:
        tree[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        tree[y_root] = x_root
    else:
        tree[y_root] = x_root
        rank[x_root] + 1


# main
n, m = map(int, input().split())

tree = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(rank, tree, a, b)
    else:
        if find(tree, a) == find(tree, b):
            print("YES")
        else:
            print("NO")
