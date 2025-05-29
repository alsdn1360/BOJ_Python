# main
n = int(input())

houses = []

for _ in range(n):
    l, h = map(int, input().split())
    houses.append((l, h))

houses.sort()
highest_height = max(houses, key=lambda x: x[1])[1]

# 가장 높은 기둥 구간의 시작, 끝 x좌표
max_housess = [h for h in houses if h[1] == highest_height]
left = min(max_housess)[0]
right = max(max_housess)[0]

area = 0

# 왼쪽에서 최고 기둥까지
curr_height = 0
curr_x = houses[0][0]

for l, h in houses:
    if l > left:
        break

    if h > curr_height:
        area += (l - curr_x) * curr_height
        curr_height = h
        curr_x = l

area += (left - curr_x) * curr_height  # left까지 누락 방지

# 오른쪽에서 최고 기둥까지
curr_height = 0
curr_x = houses[-1][0]
for l, h in reversed(houses):
    if l < right:
        break
    if h > curr_height:
        area += (curr_x - l) * curr_height
        curr_height = h
        curr_x = l

area += (curr_x - right) * curr_height  # right까지 누락 방지

# 최고 높이 구간 더하기
area += (right - left + 1) * highest_height

print(area)
