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

# 파티에 참가하면서 결국 겹치는 사람이 있으면 그 사람들은 한 집합이 된다는 것을 이용해야 함
for _ in range(m):
    party = list(map(int, input().split()))
    parties.append(party[1:])

    # 파티의 인원이 1명이면 묶을 필요없음
    if party[0] == 1:
        continue

    for i in range(1, party[0]):
        union(people, rank, party[i], party[i + 1])

truths_roots = set()  # 진실을 아는 사람이 있는 집합의 대표(루트)들의 모임

if truths[0] != 0:
    for truth in truths[1:]:
        truths_roots.add(find(people, truth))

answer = 0

for party in parties:
    can_lie = True

    for participant in party:
        # 현재 파티 참가자들의 대표(루트)가 진실을 아는 집합의 대표에 있으면 그 집합은 진실을 전부 알고있음
        if find(people, participant) in truths_roots:
            can_lie = False
            break

    if can_lie:
        answer += 1

print(answer)
