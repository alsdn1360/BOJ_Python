def find(tree, x):
    if tree[x] == x:
        return x

    tree[x] = find(tree, tree[x])  # 경로 압축

    return tree[x]


def union(tree, rank, x, y):
    x_root = find(tree, x)
    y_root = find(tree, y)

    if rank[x_root] < rank[y_root]:
        tree[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        tree[y_root] = x_root
    else:
        tree[y_root] = x_root
        rank[x_root] += 1


# main
n, m = map(int, input().split())
truths = list(map(int, input().split()))

people = [i for i in range(n + 1)]
rank = [0] * (n + 1)

parties = []  # 파티 목록

for _ in range(m):
    party = list(map(int, input().split()))
    parties.append(party[1:])

    # 파티의 인원이 1명이면 묶을 필요없음
    if party[0] == 1:
        continue

    for i in range(1, party[0]):
        union(people, rank, party[i], party[i + 1])

truths_roots = set()  # 진실을 아는 사람들의 집합

if truths[0] != 0:
    for truth in truths[1:]:
        truths_roots.add(find(people, truth))

answer = 0

for party in parties:
    can_lie = True

    for participant in party:
        if find(people, participant) in truths_roots:
            can_lie = False
            break

    if can_lie:
        answer += 1

print(answer)
