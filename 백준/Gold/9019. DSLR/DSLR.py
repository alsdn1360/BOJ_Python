from collections import deque


def d(n):
    return (2 * n) % 10000


def s(n):
    return 9999 if n == 0 else n - 1


def l(n):
    return (n % 1000) * 10 + (n // 1000)


def r(n):
    return (n % 10) * 1000 + (n // 10)


def bfs(a, b):
    queue = deque([(a, "")])
    visited = [False] * 10000
    visited[a] = True

    while queue:
        curr_digit, command = queue.popleft()

        if curr_digit == b:
            return command

        # D
        next_digit = d(curr_digit)

        if not visited[next_digit]:
            queue.append((next_digit, command + "D"))
            visited[next_digit] = True

        # S
        next_digit = s(curr_digit)

        if not visited[next_digit]:
            queue.append((next_digit, command + "S"))
            visited[next_digit] = True

        # L
        next_digit = l(curr_digit)

        if not visited[next_digit]:
            queue.append((next_digit, command + "L"))
            visited[next_digit] = True

        # R
        next_digit = r(curr_digit)

        if not visited[next_digit]:
            queue.append((next_digit, command + "R"))
            visited[next_digit] = True


# main
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(bfs(a, b))
