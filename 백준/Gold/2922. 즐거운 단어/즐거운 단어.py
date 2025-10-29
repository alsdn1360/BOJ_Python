VOWEL = ["A", "E", "I", "O", "U"]


def solve(idx, has_L, v_cnt, c_cnt):
    if v_cnt == 3 or c_cnt == 3:
        return 0

    if idx == n:
        return 1 if has_L else 0

    char = word[idx]
    cases = 0

    if char == "_":
        cases += 5 * solve(idx + 1, has_L, v_cnt + 1, 0)  # 모음을 선택하는 경우
        cases += solve(idx + 1, True, 0, c_cnt + 1)  # L을 선택하는 경우
        cases += 20 * solve(idx + 1, has_L, 0, c_cnt + 1)  # 자음을 선택하는 경우
    elif char in VOWEL:  # 모음일 때
        cases += solve(idx + 1, has_L, v_cnt + 1, 0)
    elif char == "L":  # L일 때
        cases += solve(idx + 1, True, 0, c_cnt + 1)
    else:  # 자음일 때
        cases += solve(idx + 1, has_L, 0, c_cnt + 1)

    return cases


# main
word = list(input())
n = len(word)

print(solve(0, False, 0, 0))
