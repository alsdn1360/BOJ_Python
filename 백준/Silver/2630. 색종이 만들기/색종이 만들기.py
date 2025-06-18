# 현재 칸의 모든 색이 같은지 확인
def check_area_color(color, start_i, start_j, n):
    for i in range(start_i, start_i + n):
        for j in range(start_j, start_j + n):
            if papers[i][j] == color:
                continue

            return False

    return True


# 종이 자르기
def divide(start_i, start_j, n):
    color = papers[start_i][start_j]

    if check_area_color(color, start_i, start_j, n):
        paper_cnt[color] += 1
    else:
        new_n = n // 2

        divide(start_i, start_j + new_n, new_n)  # 1사분면
        divide(start_i, start_j, new_n)  # 2사분면
        divide(start_i + new_n, start_j, new_n)  # 3사분면
        divide(start_i + new_n, start_j + new_n, new_n)  # 4사분면


# main
N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]
paper_cnt = [0, 0]  # 흰색 종이 수, 파란색 종이 수

divide(0, 0, N)

print(paper_cnt[0])
print(paper_cnt[1])
