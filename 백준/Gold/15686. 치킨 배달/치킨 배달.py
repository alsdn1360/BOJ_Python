from itertools import combinations


# main
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []  # 집 위치
chicken = []  # 치킨집 위치

for i in range(n):
    for j in range(n):
        # 1부터 시작이므로 +1
        if city[i][j] == 1:
            house.append((i + 1, j + 1))
        elif city[i][j] == 2:
            chicken.append((i + 1, j + 1))

answer = float("inf")

for selected_chicken in combinations(chicken, m):
    city_street = 0  # 도시의 치킨 거리

    for r1, c1 in house:
        street = float("inf")  # 치킨 거리

        # 하나의 집을 기준으로 선택된 치킨집의 최소 거리를 구함
        for r2, c2 in selected_chicken:
            street = min(street, abs(r1 - r2) + abs(c1 - c2))

        # 선택된 치킨집들의 도시의 치킨 거리를 구함
        city_street += street

    # 선택된 치킨집들 중 작은 도시의 치킨 거리를 구함
    answer = min(answer, city_street)

print(answer)
