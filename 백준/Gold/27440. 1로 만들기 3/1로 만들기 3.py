from collections import deque


# main
n = int(input())

queue = deque([(n, 0)])
visited = {n}

while queue:
    x, cnt = queue.popleft()

    if x == 1:
        print(cnt)
        break

    if x % 3 == 0:
        nx = x // 3

        if nx not in visited:
            queue.append((nx, cnt + 1))
            visited.add(nx)

    if x % 2 == 0:
        nx = x // 2

        if nx not in visited:
            queue.append((nx, cnt + 1))
            visited.add(nx)

    nx = x - 1

    if nx not in visited:
        queue.append((nx, cnt + 1))
        visited.add(nx)
