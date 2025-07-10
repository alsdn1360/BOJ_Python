import math, sys

input = sys.stdin.readline


def custom_round(n):
    return math.floor(n + 0.5)


# main
n = int(input())

if n == 0:
    print(0)
else:
    difficulty = []

    for _ in range(n):
        difficulty.append(int(input()))

    difficulty.sort()

    trimmed_mean = custom_round(n * 0.15)

    total = sum(difficulty[trimmed_mean : n - trimmed_mean])

    print(custom_round(total / (n - 2 * trimmed_mean)))
