from collections import deque


OPERATION = {0: "D", 1: "S", 2: "L", 3: "R"}


def d(n):
    return (2 * n) % 10000


def s(n):
    return 9999 if n == 0 else n - 1


def l(n):
    return (n % 1000) * 10 + (n // 1000)


def r(n):
    return (n % 10) * 1000 + (n // 10)


def bfs(a, b):
    queue = deque([a])

    visited = [False] * 10000
    visited[a] = True

    pre_digits = [-1] * 10000
    commands = [""] * 10000

    while queue:
        curr_digit = queue.popleft()

        if curr_digit == b:
            break

        for command, op in enumerate([d, s, l, r]):
            next_digit = op(curr_digit)

            if not visited[next_digit]:
                queue.append(next_digit)
                visited[next_digit] = True
                
                pre_digits[next_digit] = curr_digit
                commands[next_digit] = OPERATION[command]

    answer = []
    curr_digit = b

    while curr_digit != a:
        answer.append(commands[curr_digit])
        curr_digit = pre_digits[curr_digit]

    return "".join(reversed(answer))


# main
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(bfs(a, b))
