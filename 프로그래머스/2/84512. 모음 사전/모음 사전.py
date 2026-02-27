def solution(word):
    answer = 0
    
    vowel = ['A', 'E', 'I', 'O', 'U']
    weight = [781, 156, 31, 6, 1]
    
    for i, c in enumerate(word):
        answer += weight[i] * vowel.index(c) + 1

    return answer
