# main
n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

shirt_cnt = 0

for shirt in shirts:
    if shirt % t == 0:
        shirt_cnt += shirt // t
    else:
        shirt_cnt += shirt // t + 1

print(shirt_cnt)
print((n // p), (n % p))
