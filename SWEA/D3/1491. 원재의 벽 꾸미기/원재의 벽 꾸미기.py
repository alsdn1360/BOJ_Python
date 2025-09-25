from math import floor, sqrt

# main
t = int(input())

for test_case in range(1, t + 1):
    n, a, b = map(int, input().split())

    ans = float("inf")

    # i는 사용한 타일의 개수(r * c)
    for i in range(1, n + 1):
        for r in range(floor(sqrt(i)), 0, -1):
            if i % r == 0:
                c = i // r
                w = a * abs(r - c) + b * (n - i)
                ans = min(ans, w)

                break

    print(f"#{test_case} {ans}")
