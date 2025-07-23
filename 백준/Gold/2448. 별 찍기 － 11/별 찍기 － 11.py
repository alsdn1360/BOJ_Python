def solve(n, r, c):
    if n == 3:
        paper[r][c] = "*"
        paper[r + 1][c - 1], paper[r + 1][c + 1] = "*", "*"
        for i in range(-2, 3):
            paper[r + 2][c + i] = "*"

        return

    nxt_n = n // 2

    solve(nxt_n, r, c)
    solve(nxt_n, r + nxt_n, c - nxt_n)
    solve(nxt_n, r + nxt_n, c + nxt_n)


# main
n = int(input())
paper = [[" " for _ in range(2 * n)] for _ in range(n)]

solve(n, 0, n - 1)

for star in paper:
    print(*star, sep="")
