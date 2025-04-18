from collections import deque


def bfs(n, k):
    queue = deque([(n, 0)])
    visited = [False] * 200001
    visited[n] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time

        for nx in (x - 1, x + 1, abs(x * 2)):
            if nx <= 200000 and not visited[nx]:
                queue.append((nx, time + 1))
                visited[nx] = True


# main
n, k = map(int, input().split())

print(bfs(n, k))
