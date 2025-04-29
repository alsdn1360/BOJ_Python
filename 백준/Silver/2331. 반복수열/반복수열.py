from collections import defaultdict


def dfs(p, permu, curr_num):
    next_num = sum(int(num) ** p for num in str(curr_num))

    if permu[next_num] < 2:
        permu[next_num] += 1
        dfs(p, permu, next_num)


# main
a, p = map(int, input().split())

permu = defaultdict(int)
permu[a] = 1

dfs(p, permu, a)

print(list(permu.values()).count(1))
