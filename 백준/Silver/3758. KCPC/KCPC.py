# main
T = int(input())

for _ in range(T):
    # 팀의 개수, 문제의 개수, 우리 팀의 ID, 로그 엔트리 개수
    n, k, t, m = map(int, input().split())

    # 점수
    team = [[(0) for _ in range(k)] for _ in range(n)]
    # 총 점수, 제출 횟수, 마지막 제출 시각
    team_info = [(0, 0, 0) for _ in range(n)]

    for submit in range(m):
        # 팀 ID, 문제 번호, 점수
        i, j, s = map(int, input().split())

        team[i - 1][j - 1] = max(team[i - 1][j - 1], s)
        team_info[i - 1] = (sum(team[i - 1]), team_info[i - 1][1] + 1, submit)

    sorted_team_info = sorted(team_info, key=lambda x: (-x[0], x[1], x[2]))

    print(sorted_team_info.index(team_info[t - 1]) + 1)
