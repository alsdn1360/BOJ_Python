def bt(start):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(start, n + 1):
        answer.append(i)

        bt(i)

        answer.pop()


# main
n, m = map(int, input().split())

answer = []
pre_answer = []

bt(1)
