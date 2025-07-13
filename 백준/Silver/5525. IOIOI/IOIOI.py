import sys

input = sys.stdin.readline

# main
n = int(input())
m = int(input())
s = input().rstrip()

i = 0
answer = 0
cnt = 0

while i < m - 2:
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1

        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1

print(answer)
