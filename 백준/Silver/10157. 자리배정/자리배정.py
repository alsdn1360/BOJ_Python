import sys

input = sys.stdin.readline

# 하, 우, 상, 좌
MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < r and 0 <= ny < c


# main
c, r = map(int, input().split())
k = int(input())

if c * r < k:
    print(0)
    sys.exit()

seats = [[0 for _ in range(c)] for _ in range(r)]

x, y, dir = 0, 0, 0
dx, dy = MOVES[dir]

for cnt in range(1, k):
    seats[x][y] = cnt

    if not in_bound(x + dx, y + dy) or seats[x + dx][y + dy] != 0:
        dir = (dir + 1) % 4
        dx, dy = MOVES[dir]

    x, y = x + dx, y + dy

print(y + 1, x + 1)
