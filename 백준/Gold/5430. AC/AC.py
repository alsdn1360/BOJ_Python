from collections import deque
import sys

input = sys.stdin.readline

# main
t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1]

    if n > 0:
        x = deque(x.split(","))
    else:
        x = deque()

    is_reverse = False
    is_error = False

    for oper in p:
        if oper == "R":
            is_reverse = not is_reverse
        else:
            if not x:
                is_error = True
                break

            if is_reverse:
                x.pop()
            else:
                x.popleft()

    if is_error:
        print("error")
    else:
        if is_reverse:
            x.reverse()

        print(f'[{",".join(x)}]')
