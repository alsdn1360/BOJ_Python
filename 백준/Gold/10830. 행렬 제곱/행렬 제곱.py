def square_matrix(m1, m2):
    new_m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_m[i][j] += (m1[i][k] * m2[k][j]) % 1000

    return new_m


def power(a, b):
    if b == 1:
        return a

    x = power(a, b // 2)

    if b % 2 == 0:
        return square_matrix(x, x)
    else:
        return square_matrix(square_matrix(x, x), a)


# main
n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

new_matrix = power(matrix, b)

for i in range(n):
    for j in range(n):
        new_matrix[i][j] %= 1000

for row in new_matrix:
    print(*row)
