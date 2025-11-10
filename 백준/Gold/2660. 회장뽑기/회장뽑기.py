from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def bfs(start):
    queue = deque([(start, 0)])  # 시작 회원, 친구 몇 단계인지
    visited = {start}

    max_step = 0

    while queue:
        curr_member, step = queue.popleft()

        max_step = max(max_step, step)

        for friend in members[curr_member]:
            if friend not in visited:
                queue.append((friend, step + 1))
                visited.add(friend)

    # 현재 회원에게서 각 회원에게로 갈 수 있는 거리(친구 단계) 중에서 가장 큰 거리가 점수임
    return max_step


# main
n = int(input())

members = defaultdict(list)

while True:
    u, v = map(int, input().split())

    if u == -1 and v == -1:
        break

    members[u].append(v)
    members[v].append(u)

scores = [0] * n

for member in range(n):
    scores[member] = bfs(member + 1)

president_score = min(scores)
president_candidate = []

for member, score in enumerate(scores):
    if score == president_score:
        president_candidate.append(member + 1)

print(president_score, len(president_candidate))
print(*president_candidate)
