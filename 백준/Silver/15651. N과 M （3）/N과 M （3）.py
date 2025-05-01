def bt():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(1, n + 1):
        answer.append(i)

        bt()

        answer.pop()


# main
n, m = map(int, input().split())
answer = []

bt()
