from collections import deque


def in_bound(nx):
    return 0 <= nx <= 100000


def bfs(n, k):
    queue = deque([n])

    visited = [False] * 100001
    time = [0] * 100001  # 최단 시간
    cnt = [0] * 100001  # 최단 시간으로 찾는 방법의 수

    visited[n] = True
    cnt[n] = 1

    while queue:
        x = queue.popleft()
        curr_time = time[x]
        curr_cnt = cnt[x]

        for nx in (x - 1, x + 1, 2 * x):
            if in_bound(nx):
                if not visited[nx]:  # 첫 방문 했을 때
                    queue.append(nx)
                    visited[nx] = True
                    time[nx] = curr_time + 1
                    cnt[nx] = curr_cnt
                elif time[nx] == curr_time + 1:  # 방문했었지만, 또 최단 시간일 때
                    cnt[nx] += curr_cnt

    return time[k], cnt[k]


# main
n, k = map(int, input().split())

time, cnt = bfs(n, k)

print(f"{time}\n{cnt}")
