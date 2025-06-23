n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        nums[i][j] += max(nums[i + 1][j], nums[i + 1][j + 1])

print(nums[0][0])
