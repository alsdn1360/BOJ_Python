VOWELS = {"a", "e", "i", "o", "u"}


def bt(start):
    cons_cnt = sum(1 for ch in answer if ch not in VOWELS)

    if len(answer) == l and set(answer) & VOWELS and cons_cnt > 1:
        print("".join(answer))
        return

    for i in range(start, c):
        alp = alps[i]

        answer.append(alp)

        bt(i + 1)

        answer.pop()


# main
l, c = map(int, input().split())
alps = sorted(list(map(str, input().split())))
answer = []

bt(0)
