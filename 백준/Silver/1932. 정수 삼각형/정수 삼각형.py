# main
n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    nums_j = len(nums[i])

    for j in range(nums_j):
        if j == 0:
            nums[i][j] += nums[i - 1][j]
        elif j == nums_j - 1:
            nums[i][j] += nums[i - 1][j - 1]
        else:
            nums[i][j] += max(nums[i - 1][j], nums[i - 1][j - 1])

print(max(nums[n - 1]))
