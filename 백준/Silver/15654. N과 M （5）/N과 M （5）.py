def bt():
    if len(answer) == m:
        print(*answer)
        return

    for num in nums:
        if num not in answer:
            answer.append(num)

            bt()

            answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []

bt()
