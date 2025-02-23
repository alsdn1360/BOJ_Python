def find(tree, x):
    if tree[x] == x:
        return x
    
    # 경로 압축: 해당 집합에서 루트를 제외한 모든 노드의 부모 노드를 루트로 바꿈
    tree[x] = find(tree, tree[x])
    
    return tree[x]

def union(tree, rank, x, y):
    xroot = find(tree, x)
    yroot = find(tree, y)
    
    # 랭크가 작은 트리를 랭크가 큰 트리에 연결
    # 랭크가 작은 트리의 루트를 랭크가 큰 트리의 루트로 바꾸는 것
    if rank[xroot] < rank[yroot]:
        tree[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        tree[yroot] = xroot
    # 같으면 아무것나 골라서 연결하고, 연결되어서 랭크가 더 커졌으므로 랭크가 큰 트리에 랭크를 1 더함
    else:
        tree[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    # 비용이 작은 간선부터 선택해야 최소 신장 트리를 만들 수 있기 때문에 오름차순 정렬
    costs.sort(key = lambda x : x[2])
    
    tree = [i for i in range(n)]
    rank = [0] * n

    # 최소 신장 트리의 총 비용
    min_cost = 0
    # 최소 신장 트리에 포함된 간선의 개수
    edges = 0
    
    for edge in costs:
        # 최소 신장 트리의 속성에 의해 종료
        if edges == n - 1:
            break
            
        x = find(tree, edge[0])
        y = find(tree, edge[1])
        
        # 두 노드가 서로 다른 집합에 속하는 경우(루트 노드가 다름)
        if x != y:
            union(tree, rank, x, y)
            min_cost += edge[2]
            edges += 1
            
    return min_cost