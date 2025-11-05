# 블럭들 상대 높이
BLOCKS = {
    1: [[], [0, 0, 0]],
    2: [[0]],
    3: [[0, 1], [-1]],
    4: [[-1, -1], [1]],
    5: [[0, 0], [-1], [-1, 0], [1]],
    6: [[0, 0], [0], [1, 1], [-2]],
    7: [[0, 0], [0], [0, -1], [2]],
}

# main
c, p = map(int, input().split())
h = list(map(int, input().split()))

block = BLOCKS[p]

answer = 0

for curr_c, curr_h in enumerate(h):
    for b in block:
        b_w = len(b) + 1  # 현재 블록 너비

        # 최대 열 넘어가면 패스
        if curr_c + b_w > c:
            continue

        is_match = True

        for nxt_c, relative_h in enumerate(b, start=1):
            if h[curr_c + nxt_c] - curr_h != relative_h:
                is_match = False
                break

        if is_match:
            answer += 1

print(answer)
