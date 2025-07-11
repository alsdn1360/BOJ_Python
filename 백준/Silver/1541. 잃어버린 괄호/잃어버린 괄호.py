# main
equation = input()

nums = equation.split("-")

for i, num in enumerate(nums):
    if "+" in num:
        nums[i] = sum(map(int, num.split("+")))
    else:
        nums[i] = int(nums[i])

answer = nums[0]

for num in nums[1:]:
    answer -= num

print(answer)
