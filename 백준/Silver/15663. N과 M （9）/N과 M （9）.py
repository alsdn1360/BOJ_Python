def bt():
    depl = tuple(answer)

    if len(answer) == m and depl not in prev:
        print(*answer)
        prev.add(depl)
        return

    for i, num in enumerate(nums):
        if not visited[i]:
            answer.append(num)
            visited[i] = True

            bt()

            visited[i] = False
            answer.pop()


# main
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = []
visited = [False] * n
prev = set()

bt()
