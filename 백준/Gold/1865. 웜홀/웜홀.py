import sys

input = sys.stdin.readline

def bellman_ford():
    dists = {node: 0 for node in range(1, n + 1)}

    for i in range(n):
        for curr_node in range(1, n + 1):
            for adj_node, adj_dist in road[curr_node]:
                if dists[adj_node] > dists[curr_node] + adj_dist:
                    dists[adj_node] = dists[curr_node] + adj_dist

                    # 음수 사이클 존재 여부 확인
                    if i == n - 1:
                        # 음수 사이클이 있음
                        # 문제에서는 시간이 음수가 되어야 하므로 YES 출력
                        return "YES"

    return "NO"


# main
tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    road = {node: [] for node in range(1, n + 1)}

    for _ in range(m):
        s, e, t = map(int, input().split())
        road[s].append((e, t))
        road[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        road[s].append((e, -t))

    print(bellman_ford())
