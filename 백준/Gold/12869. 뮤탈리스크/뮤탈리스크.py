from collections import deque


ATTACK = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]


def bfs(scvs):
    queue = deque([(scvs, 0)])

    visited = [[[False for _ in range(61)] for _ in range(61)] for _ in range(61)]
    visited[scvs[0]][scvs[1]][scvs[2]] = True

    while queue:
        (scv1, scv2, scv3), cnt = queue.popleft()

        if scv1 <= 0 and scv2 <= 0 and scv3 <= 0:
            return cnt

        for atk1, atk2, atk3 in ATTACK:
            n_scv1, n_scv2, n_scv3 = max(0, scv1 - atk1), max(0, scv2 - atk2), max(0, scv3 - atk3)

            if not visited[n_scv1][n_scv2][n_scv3]:
                queue.append((sorted([n_scv1, n_scv2, n_scv3]), cnt + 1))
                visited[n_scv1][n_scv2][n_scv3] = True


# main
n = int(input())
scvs = list(map(int, input().split()))

if len(scvs) == 2:
    scvs.extend([0])
elif len(scvs) == 1:
    scvs.extend([0, 0])

print(bfs(sorted(scvs)))
