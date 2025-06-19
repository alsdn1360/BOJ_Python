def divide(n, r, c, cnt):
    if n == 0:
        print(cnt)
        return

    size = 2**n
    half_size = 2 ** (n - 1)

    prev_cnt = half_size**2

    # 현재 (r, c)의 위치에 따라서 (r, c)와 cnt 값을 바꿔줌
    if 0 <= r < half_size and 0 <= c < half_size:  # 왼쪽 위
        divide(n - 1, r, c, cnt)
    elif 0 <= r < half_size and half_size <= c < size:  # 오른쪽 위
        divide(n - 1, r, c - half_size, cnt + prev_cnt)
    elif half_size <= r < size and 0 <= c < half_size:  # 왼쪽 아래
        divide(n - 1, r - half_size, c, cnt + prev_cnt * 2)
    else:  # 오른쪽 아래
        divide(n - 1, r - half_size, c - half_size, cnt + prev_cnt * 3)


# main
n, r, c = map(int, input().split())

divide(n, r, c, 0)
