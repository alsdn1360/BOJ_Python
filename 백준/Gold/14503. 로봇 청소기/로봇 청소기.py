from collections import deque

MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs():
    queue = deque([(r, c, d, 0)])

    visited = [[False for _ in range(m)] for _ in range(n)]

    while queue:
        x, y, dirc, clean = queue.popleft()

        is_clean = False

        # 1번 작동
        if not visited[x][y] and room[x][y] == 0:
            clean += 1
            visited[x][y] = True
        else:
            visited[x][y] = True

        # 2, 3번 중 어떤 선택을 해야할지 체크
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy

            if in_bound(nx, ny) and not visited[nx][ny] and room[nx][ny] == 0:
                is_clean = True
                break

        if not is_clean:
            nx, ny = x - MOVES[dirc][0], y - MOVES[dirc][1]

            if in_bound(nx, ny) and room[nx][ny] == 0:
                # 2-1번 작동
                queue.append((nx, ny, dirc, clean))
            else:
                # 2-2번 작동
                return clean
        else:
            # 3-1번 작동
            dirc = (dirc - 1) % 4

            nx, ny = x + MOVES[dirc][0], y + MOVES[dirc][1]

            if in_bound(nx, ny) and not visited[nx][ny] and room[nx][ny] == 0:
                # 3-2번 작동
                queue.append((nx, ny, dirc, clean))
            else:
                # 3-3번 작동
                queue.append((x, y, dirc, clean))


# main
n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

print(bfs())
