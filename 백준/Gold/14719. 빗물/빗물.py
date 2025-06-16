# main
h, w = map(int, input().split())
block_h = list(map(int, input().split()))

rain = 0

for i in range(1, w - 1):
    curr_h = block_h[i]
    wall_h = min(max(block_h[:i]), max(block_h[i:]))

    if curr_h >= wall_h:
        continue

    rain += wall_h - curr_h

print(rain)
