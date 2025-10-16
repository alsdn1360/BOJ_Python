import sys

input = sys.stdin.readline


# 시계방향으로 120도 회전
def rotate_clockwise(a):
    rotated_a = [[0 for _ in range(i + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            rotated_a[(n - 1) - (i - j)][(n - 1) - i] = a[i][j]

    return rotated_a


# 반시계방향으로 120도 회전
def rotate_counter_clockwise(a):
    rotated_a = [[0 for _ in range(i + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            rotated_a[(n - 1) - j][i - j] = a[i][j]

    return rotated_a


# 수평으로 대칭
def mirror_horizontal(a):
    mirror_a = [[0 for _ in range(i + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            mirror_a[i][i - j] = a[i][j]

    return mirror_a


def compare(a, b):
    cnt = 0

    for i in range(n):
        for j in range(i + 1):
            if a[i][j] != b[i][j]:
                cnt += 1

    return cnt


# main
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

a_states = [a, rotate_clockwise(a), rotate_counter_clockwise(a)]

ans = float("inf")

for state in a_states:
    ans = min(ans, compare(state, b))
    ans = min(ans, compare(mirror_horizontal(state), b))  # 회전시킨 a에 대해서 대칭시킨 것도 바로 비교

print(ans)
