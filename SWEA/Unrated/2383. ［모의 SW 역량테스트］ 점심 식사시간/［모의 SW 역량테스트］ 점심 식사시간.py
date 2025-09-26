import heapq
from itertools import combinations


def manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def simulate(s1_p, s2_p):
    # 각 그룹에 대한 계단 입구 도착 시간
    s1_arrival_t = sorted([manhattan_dist(pr, pc, s[0][0], s[0][1]) for pr, pc in s1_p])
    s2_arrival_t = sorted([manhattan_dist(pr, pc, s[1][0], s[1][1]) for pr, pc in s2_p])

    t = 0
    end_p = 0

    s1_p_idx, s2_p_idx = 0, 0

    s1, s2 = [], []  # 계단
    s1_queue, s2_queue = [], []  # 계단 대기 큐

    total_p = len(s1_p) + len(s2_p)

    while end_p < total_p:
        # 1. 이동 완료한 사람 처리
        while s1 and s1[0] == t:
            heapq.heappop(s1)
            end_p += 1

        while s2 and s2[0] == t:
            heapq.heappop(s2)
            end_p += 1

        # 2. 계단 입구에 도착한 사람을 대기 큐에 넣기
        while s1_p_idx < len(s1_arrival_t) and s1_arrival_t[s1_p_idx] == t:
            heapq.heappush(s1_queue, t + 1)
            s1_p_idx += 1

        while s2_p_idx < len(s2_arrival_t) and s2_arrival_t[s2_p_idx] == t:
            heapq.heappush(s2_queue, t + 1)
            s2_p_idx += 1

        # 3. 대기 큐에 있는 사람을 계단으로 보내기
        while s1_queue and len(s1) < 3:
            heapq.heappop(s1_queue)
            heapq.heappush(s1, t + k[0])

        while s2_queue and len(s2) < 3:
            heapq.heappop(s2_queue)
            heapq.heappush(s2, t + k[1])

        t += 1

    return t


# main
tc = int(input())

for test_case in range(1, tc + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]

    p, s, k = [], [], []  # 사람 위치, 계단 위치(반드시 2개), 계단별 걸리는 시간

    # 사람, 계단 위치, 계단별 걸리는 시간 파악
    for i in range(n):
        for j in range(n):
            num = room[i][j]

            if num == 0:
                continue
            elif num == 1:
                p.append((i, j))
            else:
                s.append((i, j))
                k.append(num)

    ans = float("inf")
    p_indices = range(len(p))

    for i in range(len(p) + 1):
        # 1번 계단으로 가는 사람들의 집합 구하기
        for s1_indices in combinations(p_indices, i):
            s1_p, s2_p = [], []  # 1번 계단 그룹, 2번 계단 그룹

            for idx in p_indices:
                if idx in s1_indices:
                    s1_p.append(p[idx])
                else:
                    s2_p.append(p[idx])

            ans = min(ans, simulate(s1_p, s2_p))

    print(f"#{test_case} {ans}")
