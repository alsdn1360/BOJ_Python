def solve(nxt_num, curr_exp):
    if nxt_num > n:
        result = eval(curr_exp.replace(" ", ""))

        if result == 0:
            answer.append(curr_exp)

        return

    # '+'일 때
    solve(nxt_num + 1, curr_exp + "+" + str(nxt_num))

    # '-'일 때
    solve(nxt_num + 1, curr_exp + "-" + str(nxt_num))

    # 공백일 때
    solve(nxt_num + 1, curr_exp + " " + str(nxt_num))


# main
t = int(input())

for _ in range(t):
    n = int(input())

    answer = []

    solve(2, "1")

    print(*sorted(answer), sep="\n")
    print()
