from itertools import combinations


def get_p(base, selected_nodes):
    p = 0

    for i, j in selected_nodes:
        p += abs(i - base[0]) + abs(j - base[1])

    return p


def get_u(selected_nodes):
    a, b, c, d = float("inf"), float("inf"), 0, 0

    for i, j in selected_nodes:
        a, b, c, d = min(a, i), min(b, j), max(c, i), max(d, j)

    return (c + 1 - a) * (d + 1 - b)  # 0-indexed 보정으로 +1


def get_max_c(nodes, k, base):
    max_c = 0

    for selected_nodes in combinations(nodes, k):
        p = get_p(base, selected_nodes)
        u = get_u(selected_nodes)

        max_c = max(max_c, max(p - u, 0))

    return max_c


# main
n, m, k1, k2 = map(int, input().split())
village = [list(input()) for _ in range(n)]

base = None  # 기지국 위치
nodes = []

for i in range(n):
    for j in range(n):
        if village[i][j] == "B":
            base = (i, j)
        elif village[i][j] == "N":
            nodes.append((i, j))

max_c_noon = get_max_c(nodes, k1, base)
max_c_night = get_max_c(nodes, k2, base)

print(max_c_noon)
print(max_c_night)
