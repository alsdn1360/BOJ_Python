from collections import Counter

# main
answer = 0

n = int(input())

target = input()
target_len = len(target)
target_cnt = Counter(target)

for _ in range(n - 1):
    word = input()
    word_len = len(word)
    word_cnt = Counter(word)

    diff_len = abs(target_len - word_len)

    if diff_len == 0:
        # 길이가 같으면 하나의 문자만 달라야 함(그 문자만 바꾸면 됨)
        diff_chars = sum((target_cnt - word_cnt).values())

        if diff_chars <= 1:
            answer += 1
    elif diff_len == 1:
        # 길이 차이가 1이면 한 문자만 하나 더 있어야 함
        if target_len > word_len:
            diff_chars = sum((target_cnt - word_cnt).values())
        else:
            diff_chars = sum((word_cnt - target_cnt).values())

        if diff_chars == 1:
            answer += 1

print(answer)
