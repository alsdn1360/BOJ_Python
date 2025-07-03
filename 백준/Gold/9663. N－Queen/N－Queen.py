def check_queen(new_r, new_c):
    # 0 ~ (r - 1)행까지 이전의 놓인 퀸들의 위치 확인
    for prev_r in range(new_r):
        prev_c = col[prev_r]

        if prev_c == new_c or abs(new_r - prev_r) == abs(new_c - prev_c):
            return False

    return True


def place_queen(r):
    if r == n:
        return 1

    cnt = 0

    for c in range(n):
        if check_queen(r, c):
            col[r] = c

            cnt += place_queen(r + 1)

            col[r] = -1  # 백트래킹

    return cnt


# main
n = int(input())

col = [-1] * n  # col[i] = j: i번째 행에는 j번 열에 퀸이 있음을 저장한 배열

print(place_queen(0))
