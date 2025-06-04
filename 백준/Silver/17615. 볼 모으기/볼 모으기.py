import sys

input = sys.stdin.readline

# main
answer = float("inf")

n = int(input())
balls = list(input().rstrip())

r_balls = []
b_balls = []

for i, ball in enumerate(balls):
    if ball == "R":
        r_balls.append(i)
    else:
        b_balls.append(i)

r_left = 0
r_right = 0
b_left = 0
b_right = 0

r_n = n - 1
b_n = n - 1

# 빨간공 왼쪽에 몰려있는지 확인
for i, r_b in enumerate(r_balls):
    if i != r_b:
        r_left += 1

# 빨간공 오른쪽에 몰려있는지 확인
for r_b in reversed(r_balls):
    if r_n != r_b:
        r_right += 1

    r_n -= 1

# 파란공 왼쪽에 몰려있는지 확인
for i, b_b in enumerate(b_balls):
    if i != b_b:
        b_left += 1

# 빨간공 오른쪽에 몰려있는지 확인
for b_b in reversed(b_balls):
    if b_n != b_b:
        b_right += 1

    b_n -= 1

print(min(r_left, r_right, b_left, b_right))
