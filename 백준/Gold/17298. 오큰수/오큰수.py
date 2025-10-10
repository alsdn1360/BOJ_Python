import sys

input = sys.stdin.readline

# main
n = int(input())
a = list(map(int, input().split()))

stack = []  # 아직 오큰수를 찾지 못한 A의 인덱스를 넣어줌
nge = [-1] * n

for i in range(n):
    # 현재 수가 스택의 마지막 값(인덱스)보다 클 때까지 계속함
    while stack and a[i] > a[stack[-1]]:
        nge[stack[-1]] = a[i]
        stack.pop()

    stack.append(i)

print(*nge)
