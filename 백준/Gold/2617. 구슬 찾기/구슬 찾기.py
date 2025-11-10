from collections import deque
import sys

input = sys.stdin.readline


def bfs(start, beads):
    queue = deque([(start, 1)])
    visited = {start}

    while queue:
        curr_bead, cnt = queue.popleft()

        for relevant_bead in beads[curr_bead]:
            if relevant_bead not in visited:
                queue.append((relevant_bead, cnt + 1))
                visited.add(relevant_bead)

    return len(visited) - 1


# main
n, m = map(int, input().split())

heavy_beads = {node: [] for node in range(1, n + 1)}  # 자신보다 더 가벼운 구슬 번호들
light_beads = {node: [] for node in range(1, n + 1)}  # 자신보다 더 무거운 구슬 번호들

for _ in range(m):
    a, b = map(int, input().split())
    heavy_beads[a].append(b)
    light_beads[b].append(a)

answer = 0
mean_bead = (n + 1) // 2

for bead in range(1, n + 1):
    if bfs(bead, heavy_beads) >= mean_bead or bfs(bead, light_beads) >= mean_bead:
        answer += 1

print(answer)
