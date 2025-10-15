from math import factorial

MOD = 10**9 + 7


def get_child_num(parent_num, gen, d_i):
    return (prev_j[gen - 1] + (parent_num - prev_j[gen - 2] - 1) * gen + d_i) % MOD


# main
n = int(input())
d = list(map(int, input().split()))

# 정민수의 누적합
prev_j = [0] * 100

for i in range(1, 100):
    prev_j[i] += (prev_j[i - 1] + factorial(i)) % MOD

parent_num = 1  # 첫 부모 번호

for gen, d_i in enumerate(d, start=1):
    if gen == 1:
        print(1)
        continue

    child_num = get_child_num(parent_num, gen, d_i)

    print(child_num)

    parent_num = child_num
