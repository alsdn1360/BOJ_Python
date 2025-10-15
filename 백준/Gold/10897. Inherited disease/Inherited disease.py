from math import factorial


def get_curr_child_num(parent_num, gen, child_num):
    return (prev_j[gen - 1] + (parent_num - prev_j[gen - 2] - 1) * gen + child_num) % 1000000007


# main
n = int(input())
d = list(map(int, input().split()))

# 정민수의 누적합
prev_j = [0] * 100

for i in range(1, 100):
    prev_j[i] += (prev_j[i - 1] + factorial(i)) % 1000000007

curr_parent_num = 1

for i, d_i in enumerate(d):
    if i + 1 == 1:
        print(1)
        continue

    curr_child_num = get_curr_child_num(curr_parent_num, i + 1, d_i)
    print(curr_child_num)
    curr_parent_num = curr_child_num
