from collections import deque
import sys

input = sys.stdin.readline

# main
t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()
    x = deque(x[1:-1].split(","))

    is_reverse = False
    is_error = False

    for oper in p:
        if oper == "R":
            is_reverse = not is_reverse
        else:
            if n == 0:
                is_error = True
                break

            if is_reverse:
                x.pop()
            else:
                x.popleft()

            n -= 1

    if is_reverse:
        x.reverse()

    print("error") if is_error else print("[" + ",".join(x) + "]")
