# x, y: 집의 좌표
# i, j: 현재 중심 좌표
def check_manhattan_dist(x, y, i, j, k):
    return abs(x - i) + abs(y - j) < k


def calculate_op_cost(k):
    return k * k + (k - 1) * (k - 1)


# main
tc = int(input())

for test_case in range(1, tc + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    home = []

    # 집들의 위치 파악
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home.append((i, j))

    ans = 0

    for i in range(n):
        for j in range(n):
            # k의 값의 상한선을 2 * n으로 설정
            for k in range(1, 2 * n):
                service_home = 0

                for x, y in home:
                    if check_manhattan_dist(x, y, i, j, k):
                        service_home += 1

                # 이익이 손해가 아닐때만 갱신
                if m * service_home - calculate_op_cost(k) >= 0:
                    ans = max(ans, service_home)

    print(f"#{test_case} {ans}")
