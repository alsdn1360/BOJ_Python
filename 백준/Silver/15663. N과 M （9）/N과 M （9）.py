def bt():
    depl = tuple(answer)

    if len(answer) == m and depl not in prev:
        print(*answer)
        prev.add(depl)
        return

    for i, num in enumerate(nums):
        if i not in visited:
            answer.append(num)
            visited.append(i)

            bt()

            visited.pop()
            answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []
visited = []
prev = set()

bt()
