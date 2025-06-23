# 분할 정복을 이용한 거듭제곱
def power(a, b, c):
    if b == 1:
        return a % c

    # 지수를 2로 나눈 몫으로 재귀
    temp = power(a, b // 2, c)

    temp *= temp

    if b % 2 == 0:
        return temp % c
    else:
        return (temp * a) % c


# main
a, b, c = map(int, input().split())

print(power(a, b, c))
