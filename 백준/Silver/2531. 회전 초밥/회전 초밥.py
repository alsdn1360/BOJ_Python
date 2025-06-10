from collections import deque

# main
# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())

sushis = [int(input()) for _ in range(N)]
ex_sushis = sushis + sushis  # 회전하는 벨트이므로 두개를 더해줌

eaten_sushis = [0 for _ in range(d + 1)]
for i in range(k):
    eaten_sushis[ex_sushis[i]] += 1

eaten_sushi_cnt = 0
for es in eaten_sushis:
    if es > 0:
        eaten_sushi_cnt += 1

used_coupon = eaten_sushi_cnt
if eaten_sushis[c] == 0:
    used_coupon += 1

answer = used_coupon

for i in range(1, N):
    eaten_sushis[ex_sushis[i - 1]] -= 1  # 이전에 먹은 초밥
    if eaten_sushis[ex_sushis[i - 1]] == 0:
        eaten_sushi_cnt -= 1

    eaten_sushis[ex_sushis[i - 1 + k]] += 1  # 이후에 먹을 초밥
    if eaten_sushis[ex_sushis[i - 1 + k]] == 1:
        eaten_sushi_cnt += 1

    used_coupon = eaten_sushi_cnt  # 쿠폰 사용
    if eaten_sushis[c] == 0:
        used_coupon += 1

    answer = max(answer, used_coupon)

print(answer)
