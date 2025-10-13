import sys

input = sys.stdin.readline

# main
n = int(input())
l = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))

selected_l = [0] * 10001

for p, d in l:
    if selected_l[d] == 0:
        selected_l[d] = p
    else:
        for prev_d in range(d, 0, -1):
            if selected_l[prev_d] == 0:
                selected_l[prev_d] = p
                break

print(sum(selected_l))
