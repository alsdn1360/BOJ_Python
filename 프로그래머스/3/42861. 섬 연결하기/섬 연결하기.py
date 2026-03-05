from collections import defaultdict


def find(tree, x):
    if tree[x] == x:
        return x
    
    tree[x] = find(tree, tree[x])
    
    return tree[x]


def union(tree, rank, x, y):
    x_root = find(tree, x)
    y_root = find(tree, y)
    
    if x_root == y_root:
        return
    
    if rank[x_root] < rank[y_root]:
        tree[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        tree[y_root] = x_root
    else:
        tree[y_root] = x_root
        rank[x_root] += 1


def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    
    tree = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    
    for u, v, c in costs:
        if find(tree, u) != find(tree, v):
            union(tree, rank, u, v)
            answer += c
    
    return answer
