def dfs(i):
    answer = 0
    is_break = False

    if i == n:
        return sum(1 for s, _ in eggs if s <= 0)

    if eggs[i][0] <= 0:
        return dfs(i + 1)

    for j in range(n):
        if j != i and eggs[j][0] > 0:
            is_break = True

            pre_i, pre_j = eggs[i][0], eggs[j][0]

            eggs[i][0] -= eggs[j][1]
            eggs[j][0] -= eggs[i][1]

            answer = max(answer, dfs(i + 1))

            eggs[i][0], eggs[j][0] = pre_i, pre_j

    if not is_break:
        answer = max(answer, dfs(i + 1))

    return answer


# main
n = int(input())
eggs = []

for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])

print(dfs(0))
