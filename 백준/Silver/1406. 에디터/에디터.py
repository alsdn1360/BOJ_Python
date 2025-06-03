import sys
from collections import deque

input = sys.stdin.readline

# main
char = deque(input().rstrip())
m = int(input())

diff_char = deque()

for _ in range(m):
    cmds = list(input().split())
    cmd = cmds[0]

    if char and cmd == "L":
        diff_char.appendleft(char.pop())
    elif diff_char and cmd == "D":
        char.append(diff_char.popleft())
    elif char and cmd == "B":
        char.pop()
    elif cmd == "P":
        char.append(cmds[1])

print("".join(char + diff_char))
