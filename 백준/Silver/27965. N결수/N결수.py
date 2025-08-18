# main
n, k = map(int, input().split())

rem = ''

for i in range(1, n + 1):
    rem += str(i)
    rem = str(int(rem) % k)

print(rem)
