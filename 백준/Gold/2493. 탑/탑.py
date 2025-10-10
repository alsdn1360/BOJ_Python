import sys

input = sys.stdin.readline

# main
n = int(input())
tower = list(map(int, input().split()))

stack = []
razer = [0] * n

for i in range(n - 1, -1, -1):
    while stack and tower[i] > tower[stack[-1]]:
        razer[stack[-1]] = i + 1
        stack.pop()

    stack.append(i)

print(*razer)
