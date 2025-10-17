from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(cycle_len, curr_v):
    visited.add(curr_v)

    for nxt_v in graph[curr_v]:
        if nxt_v not in visited:
            cycle_len = dfs(cycle_len + 1, nxt_v)

    return cycle_len


# main
n = int(input())
a = list(map(int, input().split()))

# 정렬된 값의 인덱스
sorted_idx = {v: i for i, v in enumerate(sorted(a))}

graph = defaultdict(list)

# 현재 인덱스에 정렬 전 값이 정렬 후에는 어느 인덱스로 이동했는지 넣음
for i, v in enumerate(a):
    graph[i].append(sorted_idx[v])

visited = set()
ans = 0

for i in range(n):
    if i not in visited:
        ans += dfs(1, i) - 1  # 길이가 k인 사이클을 정렬하려면 k-1번의 교환(swap)이 필요함

print(ans)
