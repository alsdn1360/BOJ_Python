import sys

input = sys.stdin.readline

# main
n = int(input())
happy_day = [int(input()) for _ in range(n)]

for i in range(n):
    happy_day[i] -= 1

happy_day.pop(0)

periods = set()

for arrival_day in happy_day:
    is_new_period = True

    # 이미 있는 주기로 나누어 떨어지면 새로운 주기의 배가 아님
    for period in periods:
        if arrival_day % period == 0:
            is_new_period = False
            break

    # 새로운 주기의 배의 주기만 넣음
    if is_new_period:
        periods.add(arrival_day)

print(len(periods))
