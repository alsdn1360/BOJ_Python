# main
n = int(input())
m = int(input())

city = [[float("inf") for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    city[a - 1][b - 1] = min(city[a - 1][b - 1], c)

# 자기 자신의 노선은 0으로 처리
for i in range(n):
    city[i][i] = 0

# 플로이드-워셜 알고리즘 적용
for k in range(n):
    for i in range(n):
        for j in range(n):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

# 갈 수 없는 경로를 0으로 처리
for i in range(n):
    for j in range(n):
        if city[i][j] == float("inf"):
            city[i][j] = 0

for i in range(n):
    print(*city[i])
