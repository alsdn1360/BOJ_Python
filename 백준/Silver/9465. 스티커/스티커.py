import sys

input = sys.stdin.readline

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# main
t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    # [i][0]: i번째 열에서 스티커 안뗐을 때
    # [i][1]: i번째 열에서 위 스티커 뗐을 때
    # [i][2]: i번째 열에서 아래 스티커 뗐을 때
    dp = [[0] * 3 for _ in range(n + 1)]

    dp[0][0], dp[0][1], dp[0][2] = 0, sticker[0][0], sticker[1][0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = sticker[0][i] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = sticker[1][i] + max(dp[i - 1][0], dp[i - 1][1])

    print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
