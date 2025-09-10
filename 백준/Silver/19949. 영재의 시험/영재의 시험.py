def solve(curr_problem):
    global ans

    if curr_problem == 10:
        correct_problem = 0

        for i in range(10):
            if problems[i] == problem_ans[i]:
                correct_problem += 1

        if correct_problem >= 5:
            ans += 1

        return

    for i in range(1, 6):
        if curr_problem >= 2 and problems[curr_problem - 1] == i and problems[curr_problem - 2] == i:
            continue

        problems[curr_problem] = i

        solve(curr_problem + 1)


# main
problem_ans = list(map(int, input().split()))

problems = [0] * 10
ans = 0

solve(0)

print(ans)
