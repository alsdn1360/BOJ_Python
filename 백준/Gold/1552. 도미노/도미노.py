import sys
from itertools import permutations
from collections import defaultdict

input = sys.stdin.readline

SCORE = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": -1,
    "B": -2,
    "C": -3,
    "D": -4,
    "E": -5,
    "F": -6,
    "G": -7,
    "H": -8,
    "I": -9,
}


def dfs(graph, visited, curr_v):
    visited.add(curr_v)

    nxt_v = graph[curr_v]

    if nxt_v not in visited:
        dfs(graph, visited, nxt_v)

    return


# main
n = int(input())
d = [list(input().rstrip()) for _ in range(n)]
d_idx = [[(i, j) for j in range(n)] for i in range(n)]  # 도미노 위치

min_ans = float("inf")
max_ans = float("-inf")

# 도미노에서 한 행과 한 열에는 각각 하나씩만 고를 수 있음
for perm in permutations(range(n), n):
    selected_d = []

    # 선택한 도미노의 위치 체크
    for i, j in enumerate(perm):
        selected_d.append(d_idx[i][j])

    temp_score = 1
    graph = defaultdict(int)

    # 점수 구하기
    for i, j in selected_d:
        temp_score *= SCORE[d[i][j]]
        graph[i] = j

    # 선택한 도미노들의 사이클 수 구하기
    visited = set()
    cycle_cnt = 0

    for v in graph.values():
        if v not in visited:
            dfs(graph, visited, v)
            cycle_cnt += 1

    # 최종 점수 확인
    if cycle_cnt % 2 == 0:
        temp_score *= -1

    min_ans = min(min_ans, temp_score)
    max_ans = max(max_ans, temp_score)

print(min_ans)
print(max_ans)
