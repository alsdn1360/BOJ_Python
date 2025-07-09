def matrix_multiply(a, b):
    c = [[0 for _ in range(2)] for _ in range(2)]

    c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007

    return c


def power(a, n):
    if n == 1:
        return a

    x = power(a, n // 2)

    if n % 2 == 0:
        return matrix_multiply(x, x)
    else:
        return matrix_multiply(matrix_multiply(x, x), a)


# main
n = int(input())

fibo = power([[1, 1], [1, 0]], n)

print(fibo[1][0])
