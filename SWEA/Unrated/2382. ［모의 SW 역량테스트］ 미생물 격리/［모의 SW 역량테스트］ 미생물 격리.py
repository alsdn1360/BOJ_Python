# 상: 0, 하: 1, 좌: 2, 우: 3
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_red_cell(nx, ny):
    return nx in {0, n - 1} or ny in {0, n - 1}


def solve(micro):
    # 1. 이번 시간에 미생물이 있을 장소 새로 만듦
    new_area = [[[] for _ in range(n)] for _ in range(n)]

    # 2. 미생물 이동
    for x, y, num, d in micro:
        nx, ny = x + MOVES[d][0], y + MOVES[d][1]

        # 약품에 미생물이 처리됨
        if check_red_cell(nx, ny):
            num //= 2
            d = d + 1 if d % 2 == 0 else d - 1  # 짝수면 +1, 아니면 -1

        # 미생물의 수가 0이 아닐때만 이동
        if num != 0:
            new_area[nx][ny].append((num, d))

    # 다시 미생물의 정보를 나타내는 리스트에 넣어줌
    new_micro = []

    # 3. 동일한 위치에 있는 미생물 처리
    for x in range(n):
        for y in range(n):
            cell = new_area[x][y]
            cell_n = len(cell)

            # 셀 하나에 군집이 한 개인 경우
            if cell_n == 1:
                new_micro.append((x, y, cell[0][0], cell[0][1]))
            # 셀 하나에 군집이 여러 개인 경우
            elif cell_n > 1:
                combined_num = 0
                max_micro_num = 0
                new_d = -1

                for c in cell:
                    combined_num += c[0]

                    if max_micro_num < c[0]:
                        max_micro_num = c[0]
                        new_d = c[1]

                new_micro.append((x, y, combined_num, new_d))

    return new_micro


# main
tc = int(input())

for test_case in range(1, tc + 1):
    n, m, k = map(int, input().split())
    micro = [(x, y, num, d - 1) for x, y, num, d in (map(int, input().split()) for _ in range(k))]

    for _ in range(m):
        micro = solve(micro)

    ans = sum(num for _, _, num, _ in micro)

    print(f"#{test_case} {ans}")
