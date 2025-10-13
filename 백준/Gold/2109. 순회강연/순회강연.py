import sys

input = sys.stdin.readline

# main
n = int(input())
l = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))

selected_l = [0] * 10001

for p, d in l:
    for selectd_d in range(d, 0, -1):
        if selected_l[selectd_d] == 0:
            selected_l[selectd_d] = p
            break

print(sum(selected_l))
