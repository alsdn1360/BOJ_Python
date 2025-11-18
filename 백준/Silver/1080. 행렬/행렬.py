import sys

input = sys.stdin.readline


def check_same():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False

    return True


def reverse_A(s_i, s_j):
    for i in range(s_i, s_i + 3):
        for j in range(s_j, s_j + 3):
            A[i][j] = (A[i][j] + 1) % 2  # 0 -> 1, 1 -> 0 뒤집기


# main
N, M = map(int, input().split())

A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

answer = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reverse_A(i, j)
            answer += 1

if check_same():
    print(answer)
else:
    print(-1)
