# main
def bt(start):
    if len(answer) == m:
        print(*sorted(answer))
        prev.add(tuple(answer))

        return

    for i in range(start, n):
        num = nums[i]

        answer.append(num)

        if tuple(answer) not in prev:
            bt(i)

        answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []
prev = set()

bt(0)
