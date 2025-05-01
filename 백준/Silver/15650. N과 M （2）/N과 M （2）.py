def bt():
    dup_answer = sorted(answer)

    if len(answer) == m and dup_answer not in pre_answer:
        print(*answer)

        pre_answer.append(dup_answer)

        return

    for i in range(1, n + 1):
        if i not in answer:
            answer.append(i)

            bt()

            answer.pop()


# main
n, m = map(int, input().split())

answer = []
pre_answer = []

bt()
