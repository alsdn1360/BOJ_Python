from math import sqrt
from collections import deque


def get_dist_to_target(x, y, xt, yt):
    return sqrt((xt - x) ** 2 + (yt - y) ** 2)


def bfs():
    max_dist_in_time = 60 * v * m

    queue = deque([(xs, ys, 0)])
    visited = set()

    while queue:
        x, y, holes_cnt = queue.popleft()

        if get_dist_to_target(x, y, xt, yt) < max_dist_in_time:
            return holes_cnt

        for xh, yh in holes:
            if (xh, yh) not in visited and get_dist_to_target(x, y, xh, yh) < max_dist_in_time:
                queue.append((xh, yh, holes_cnt + 1))
                visited.add((xh, yh))

    return 0


# main
v, m = map(float, input().split())
xs, ys = map(float, input().split())
xt, yt = map(float, input().split())

holes = []

while True:
    try:
        temp = input()

        if not temp:
            break

        x, y = map(float, temp.split())
        holes.append((x, y))
    except:
        break

answer = bfs()

print(f"Yes, visiting {answer} other holes.") if answer > 0 else print("No.")
