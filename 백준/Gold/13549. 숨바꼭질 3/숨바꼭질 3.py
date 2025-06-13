from collections import deque


def in_bound(nx):
    return 0 <= nx <= 200000


def bfs(n, k):
    queue = deque([(n, 0)])

    visited = [False] * 200001
    visited[n] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time

        for nx in (x - 1, x + 1, 2 * x):
            if in_bound(nx) and not visited[nx]:
                if 2 * x == nx:
                    queue.appendleft((nx, time))
                else:
                    queue.append((nx, time + 1))

                visited[nx] = True


# main
n, k = map(int, input().split())

print(bfs(n, k))
