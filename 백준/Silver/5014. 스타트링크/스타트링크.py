from collections import deque


def bfs(f, s, g, u, d):
    queue = deque([(s, 0)])
    visited = [False] * (f + 1)
    visited[s] = True

    while queue:
        curr_f, cnt = queue.popleft()

        if curr_f == g:
            return cnt

        for new_f in (curr_f + u, curr_f - d):
            if 1 <= new_f <= f and not visited[new_f]:
                queue.append((new_f, cnt + 1))
                visited[new_f] = True

    return "use the stairs"


# main
# 건물 층 수, 강호의 현재 위치, 스타트링크 위치, 위로 이동 가능 수, 아래로 이동 가능 수
f, s, g, u, d = map(int, input().split())

print(bfs(f, s, g, u, d))
