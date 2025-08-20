import sys

input = sys.stdin.readline

MOD = 1000000007


# 분할정복을 이용한 거듭제곱
def power(a, b):
    if b == 0:
        return 1

    x = power(a, b // 2)

    if b % 2 == 0:
        return (x * x) % MOD
    else:
        return (x * x * a) % MOD


# 모듈러 역원 구하기 (페르마의 소정리 이용)
def get_mod_inverse(n):
    return power(n, MOD - 2)


# main
m = int(input())

ans = 0

for _ in range(m):
    n, s = map(int, input().split())

    # s * n^(-1) = 기댓값 (mod p)
    ans = (ans + s * get_mod_inverse(n)) % MOD

print(ans)
