from collections import deque


def manhattan(start, target):
    return abs(target[0] - start[0]) + abs(target[1] - start[1])


def bfs():
    queue = deque([0])

    visited = [False] * (n + 2)
    visited[0] = True

    while queue:
        curr_l = queue.popleft()

        if curr_l == n + 1:
            return print("happy")

        for next_l in range(n + 2):
            if not visited[next_l] and manhattan(songdo[curr_l], songdo[next_l]) <= 1000:
                queue.append(next_l)
                visited[next_l] = True

    return print("sad")


# main
t = int(input())

for _ in range(t):
    songdo = []

    n = int(input())

    songdo.append(tuple(map(int, input().split())))

    for _ in range(n):
        songdo.append(tuple(map(int, input().split())))

    songdo.append(tuple(map(int, input().split())))

    bfs()
