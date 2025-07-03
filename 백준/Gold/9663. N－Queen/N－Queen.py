def check_queen(r, c):
    if col[c] or diag1[r + c] or diag2[r - c]:
        return False

    return True


def place_queen(r):
    if r == n:
        return 1

    cnt = 0

    for c in range(n):
        if check_queen(r, c):
            col[c] = True
            diag1[r + c] = True
            diag2[r - c] = True

            cnt += place_queen(r + 1)

            col[c] = False
            diag1[r + c] = False
            diag2[r - c] = False

    return cnt


# main
n = int(input())

col = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

print(place_queen(0))
