from collections import deque
import sys

input = sys.stdin.readline

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def check_ex_air(ex_air):
    queue = deque([(0, 0)])
    ex_air[0][0] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not ex_air[nx][ny] and cheeses[nx][ny] != 1:
                queue.append((nx, ny))
                ex_air[nx][ny] = True


def check_melt_cheese(melt_cheeses, ex_air):
    for x in range(n):
        for y in range(m):
            if cheeses[x][y] != 1:
                continue

            ex_air_cnt = 0

            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy

                if ex_air[nx][ny] == True:
                    ex_air_cnt += 1

                if ex_air_cnt >= 2:
                    melt_cheeses.append((x, y))
                    break


# main
n, m = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(n)]

time = 0

while True:
    # 1. 치즈 외부 공기 파악
    ex_air = [[False for _ in range(m)] for _ in range(n)]

    check_ex_air(ex_air)

    # 2. 녹아내리는 치즈 파악
    melt_cheeses = deque()

    check_melt_cheese(melt_cheeses, ex_air)

    # 3. 녹일 치즈 있는지 확인
    if len(melt_cheeses) == 0:
        break

    # 4. 치즈 녹이기
    for x, y in melt_cheeses:
        cheeses[x][y] = 0

    # 5. 시간 증가
    time += 1

print(time)
