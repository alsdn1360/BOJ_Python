MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < r and 0 <= ny < c


def dfs(x, y, step):
    answer = step

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny) and not visited[ord(board[nx][ny]) - ord("A")]:
            visited[ord(board[nx][ny]) - ord("A")] = True

            answer = max(answer, dfs(nx, ny, step + 1))

            visited[ord(board[nx][ny]) - ord("A")] = False

    return answer


# main
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

visited = [False] * 26
visited[ord(board[0][0]) - ord("A")] = True

print(dfs(0, 0, 1))
