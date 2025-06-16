from collections import defaultdict, deque

DICE = [1, 2, 3, 4, 5, 6]


def in_bound(np):
    return 1 <= np <= 100


def bfs():
    queue = deque([(1, 0)])  # 위치, 주사위 굴린 횟수

    visited = [False] * 101
    visited[1] = True

    while queue:
        p, cnt = queue.popleft()

        if p == 100:
            return cnt

        for d in DICE:
            np = p + d

            if in_bound(np) and not visited[np]:
                if np in ladder_snake:
                    queue.append((ladder_snake[np], cnt + 1))
                    visited[ladder_snake[np]] = True
                else:
                    queue.append((np, cnt + 1))

                visited[np] = True


# main
n, m = map(int, input().split())

board = [i for i in range(101)]
ladder_snake = defaultdict(int)

# 사다리 정보
for _ in range(n):
    x, y = map(int, input().split())
    ladder_snake[x] = y

# 뱀 정보
for _ in range(m):
    u, v = map(int, input().split())
    ladder_snake[u] = v

print(bfs())
