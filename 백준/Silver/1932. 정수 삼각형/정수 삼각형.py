# main
n = int(input())

tri = []
sum_tri = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    nums = list(map(int, input().split()))
    tri.append(nums)

sum_tri[0][0] = tri[0][0]

for i in range(n - 1):
    for j in range(len(tri[i])):
        sum_tri[i + 1][j] = max(sum_tri[i + 1][j], tri[i + 1][j] + sum_tri[i][j])
        sum_tri[i + 1][j + 1] = max(
            sum_tri[i + 1][j + 1], tri[i + 1][j + 1] + sum_tri[i][j]
        )

print(max(sum_tri[n - 1]))
