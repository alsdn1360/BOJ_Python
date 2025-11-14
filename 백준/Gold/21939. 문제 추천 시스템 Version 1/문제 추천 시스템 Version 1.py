from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

# main
N = int(input())

ps = defaultdict(int)  # 문제 정보를 담고있는 딕셔너리
min_l_ps = []  # recommend -1을 위한 최소힙
max_l_ps = []  # recommend 1을 위한 최대힙

for _ in range(N):
    p, l = map(int, input().split())

    ps[p] = l
    heapq.heappush(min_l_ps, (l, p))
    heapq.heappush(max_l_ps, (-l, -p))

M = int(input())

for _ in range(M):
    line = input().split()
    cmd = line[0]
    nums = [int(l) for l in line[1:]]

    if cmd == "recommend":
        x = nums[0]

        if x == -1:
            while min_l_ps:
                l, p = heapq.heappop(min_l_ps)

                if l == ps[p]:
                    print(p)
                    heapq.heappush(min_l_ps, (l, p))
                    break

        elif x == 1:
            while max_l_ps:
                l, p = heapq.heappop(max_l_ps)

                if -l == ps[-p]:
                    print(-p)
                    heapq.heappush(max_l_ps, (l, p))
                    break
    elif cmd == "add":
        p, l = nums[0], nums[1]

        ps[p] = l
        heapq.heappush(min_l_ps, (l, p))
        heapq.heappush(max_l_ps, (-l, -p))
    elif cmd == "solved":
        ps.pop(nums[0])
