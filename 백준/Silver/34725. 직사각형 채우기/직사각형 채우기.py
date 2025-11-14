# main
N, M = map(int, input().split())

matrix = [[0 for _ in range(M // 2)] for _ in range(N // 2)]
k = 1

for i in range(N // 2):
    for j in range(M // 2):
        matrix[i][j] = k
        k += 1

for i in range(N // 2):
    matrix[i].extend(reversed(matrix[i]))

matrix.extend(reversed(matrix))

for i in range(N):
    print(*matrix[i])
