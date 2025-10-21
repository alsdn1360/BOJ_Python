import sys

input = sys.stdin.readline


def dfs(scores, pre_game):
    answer = 0

    # 초기 최대값과 카운트 계산
    initial_max = max(scores[1 : n + 1])
    initial_max_cnt = scores[1 : n + 1].count(initial_max)

    def backtrack(curr_scores, game_round, curr_max, max_cnt):
        nonlocal answer

        # 가지치기: k팀이 남은 경기를 이겨도 우승이 불가능한 경우
        k_remaining_games = sum(1 for i in range(game_round, len(pre_game)) if k in pre_game[i])
        k_possible_max = curr_scores[k] + k_remaining_games

        if curr_max > k_possible_max:
            return

        if game_round == len(pre_game):
            if curr_scores[k] == curr_max and max_cnt == 1:
                answer += 1

            return

        x, y = pre_game[game_round]

        # 1번 팀이 이겼을 때
        curr_scores[x] += 1
        new_max = curr_max
        new_cnt = max_cnt

        if curr_scores[x] > curr_max:
            new_max = curr_scores[x]
            new_cnt = 1
        elif curr_scores[x] == curr_max:
            new_cnt += 1

        backtrack(curr_scores, game_round + 1, new_max, new_cnt)

        curr_scores[x] -= 1

        # 2번 팀이 이겼을 때
        curr_scores[y] += 1
        new_max = curr_max
        new_cnt = max_cnt

        if curr_scores[y] > curr_max:
            new_max = curr_scores[y]
            new_cnt = 1
        elif curr_scores[y] == curr_max:
            new_cnt += 1

        backtrack(curr_scores, game_round + 1, new_max, new_cnt)

        curr_scores[y] -= 1

    backtrack(scores, 0, initial_max, initial_max_cnt)

    return answer


# main
n, m, k = map(int, input().split())

scores = [0] * (n + 1)
pre_game = []

for _ in range(m):
    x, y, result = map(int, input().split())

    if result == 0:
        pre_game.append((x, y))
    elif result == 1:
        scores[x] += 1
    else:
        scores[y] += 1

print(dfs(scores, pre_game))
