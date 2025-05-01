def bt(start):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(start, n):
        num = nums[i]

        answer.append(num)

        bt(i + 1)

        answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []

bt(0)
