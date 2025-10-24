import sys

input = sys.stdin.readline

# main
n = int(input())
squares = sorted(list(tuple(v for v in map(int, input().split())) for _ in range(n)), key=lambda x: (-x[0], -x[1]))

max_y = squares[0][1]
ans = squares[0][0] * squares[0][1]

for x, y in squares[1:]:
    if y <= max_y:
        continue

    if y > max_y:
        ans += x * (y - max_y)
        max_y = y
    else:
        ans += x * y

print(ans)
