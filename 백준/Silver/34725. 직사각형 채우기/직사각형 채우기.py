# main
N, M = map(int, input().split())

matrix = [[0 for _ in range(M // 2)] for _ in range(N // 2)]
k = 1

# 평행한 직사각형의 네 꼭지점을 이용한 넓이는 어차피 k에 따라서 값이 달라지지 않기 때문에
# k를 Z 모양 순서대로 채워서 좌우, 상하 반전 시켜주면 k를 꼭지점으로 하는 모든 사각형이 완성됨
for i in range(N // 2):
    for j in range(M // 2):
        matrix[i][j] = k
        k += 1

# Z 모양으로 채워진 사각형에 좌우 반전시킨 모양을 더해줌
for i in range(N // 2):
    matrix[i].extend(reversed(matrix[i]))

# 좌우반전으 더한 모양을 또 상하 반전 시킨 모양을 더해줌
matrix.extend(reversed(matrix))

for i in range(N):
    print(*matrix[i])
