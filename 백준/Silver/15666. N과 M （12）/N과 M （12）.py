def bt(start):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(start, len(nums)):
        answer.append(nums[i])

        bt(i)

        answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

answer = []

bt(0)
