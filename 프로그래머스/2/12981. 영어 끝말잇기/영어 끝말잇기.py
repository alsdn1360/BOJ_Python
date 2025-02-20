def solution(n, words):
    # 사용한 단어와 이전 단어의 마지막 글자
    used_word = set()
    prev_word = words[0][0]
    
    for i, word in enumerate(words):
        if word in used_word or word[0] != prev_word:
            # 탈락한 사람과 탈락한 차례
            # 0부터 시작했기 때문에 +1을 해줌
            return [(i % n) + 1, (i // n) + 1]
        
        used_word.add(word)
        prev_word = word[-1]
        
    return [0, 0]