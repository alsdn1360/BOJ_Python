from collections import deque


def bfs(a, b):
    queue = deque([(a, 1)])

    visited = set()
    visited.add(a)

    while queue:
        curr_n, cnt = queue.popleft()

        if curr_n == b:
            return cnt

        for nxt_n in (2 * curr_n, 10 * curr_n + 1):
            if nxt_n not in visited and nxt_n <= b:
                queue.append((nxt_n, cnt + 1))
                visited.add(nxt_n)

    return -1


# main
a, b = map(int, input().split())

print(bfs(a, b))
