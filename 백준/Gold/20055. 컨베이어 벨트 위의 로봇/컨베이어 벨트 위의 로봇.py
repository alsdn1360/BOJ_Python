from collections import deque

# main
n, k = map(int, input().split())
durability = list(map(int, input().split()))

durability = deque(durability)
robot = deque()

step = 0

while True:
    step += 1

    # 1번
    durability.rotate(1)

    for _ in range(len(robot)):
        nxt_pos = robot.popleft() + 1

        # 로봇 즉시 내리기
        if nxt_pos == n - 1:
            continue

        robot.append(nxt_pos)

    # 2번
    for pos in range(len(robot)):
        new_pos = robot[pos] + 1

        if durability[new_pos] > 0 and new_pos not in robot:
            durability[new_pos] -= 1
            robot[pos] += 1

    # 로봇 내리기
    if robot and robot[0] == n - 1:
        robot.popleft()

    # 3번
    if durability[0] > 0:
        durability[0] -= 1
        robot.append(0)

    # 4번
    if durability.count(0) >= k:
        break

print(step)
