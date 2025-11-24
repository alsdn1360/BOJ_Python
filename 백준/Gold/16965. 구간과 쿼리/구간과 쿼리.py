from collections import deque, defaultdict


def check_path(x1, y1, x2, y2):
    return x2 < x1 < y2 or x2 < y1 < y2


def bfs(a, b):
    queue = deque([a])
    visited = {a}

    while queue:
        curr_section = queue.popleft()

        if curr_section == b:
            return 1

        for adj_section in path[curr_section]:
            if adj_section not in visited:
                queue.append(adj_section)
                visited.add(adj_section)

    return 0


# main
N = int(input())

path = defaultdict(list)
sections = []

seq = 1

for _ in range(N):
    q = list(map(int, input().split()))
    cmd = q[0]

    if cmd == 1:
        x, y = q[1:]

        for s_seq, (sx, sy) in enumerate(sections, start=1):
            if check_path(x, y, sx, sy):
                path[seq].append(s_seq)

            if check_path(sx, sy, x, y):
                path[s_seq].append(seq)

        sections.append((x, y))
        seq += 1

    elif cmd == 2:
        a, b = q[1:]

        print(bfs(a, b))
