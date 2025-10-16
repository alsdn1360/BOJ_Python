import sys

input = sys.stdin.readline

# main
t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))

    # i번째 카드부터 j번째 카드까지 남아있을 때, 현재 턴인 사람이 얻을 수 있는 최대점수
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = cards[i]

    # 카드 누적합
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + cards[i]

    # 2장, 3장, 4장...이 남았을 때 최고 점수를 선택하게 함(Bottom-Up)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            score_left = cards[i] + (prefix_sum[j + 1] - prefix_sum[i + 1]) - dp[i + 1][j]  # 왼쪽 카드를 선택했을 때
            score_right = cards[j] + (prefix_sum[j] - prefix_sum[i]) - dp[i][j - 1]  # 오른쪽 카드를 선택했을 때

            dp[i][j] = max(score_left, score_right)

    # 카드 전체 개수가 있을 때 선택한 값이 답
    print(dp[0][n - 1])
