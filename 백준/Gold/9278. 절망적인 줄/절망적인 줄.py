import sys

input = sys.stdin.readline


def solve(line):
    # 가장 첫 번째 사람이 100원이면 방법이 없음
    if line[0] == ")":
        return 0

    n = len(line)

    # i번째 사람까지 줄을 세웠을 때, 그 중 50원을 들고있는 사람이 j명인 경우의 수
    dp = [[0 for _ in range(n // 2 + 1)] for _ in range(n + 1)]

    # 아무도 없는 경우의 수를 1으로 지정
    dp[0][0] = 1

    for i in range(1, n + 1):
        char = line[i - 1]

        for j in range(n // 2 + 1):
            # 50원인 사람의 경우
            if (char == "." or char == "(") and j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % 1000000

            # 100원인 사람의 경우
            # 50원을 가지고 있는 사람이 100원을 가지고 있는 사람보다 많거나 같아야 함
            if (char == "." or char == ")") and j >= i - j:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % 1000000

    return dp[n][n // 2] % 1000000


# main
while True:
    line = input().rstrip()

    if not line:
        break

    print(solve(line))
