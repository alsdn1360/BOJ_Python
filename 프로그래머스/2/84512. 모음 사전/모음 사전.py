def solution(word):
    answer = 0
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    # 해당 인덱스에 알파벳을 정하면 그 뒤에 올 알파벳의 개수
    # [(5⁰ + 5¹ + 5² + 5³ + 5⁴), (5⁰ + 5¹ + 5² + 5³), ...]
    # 각 알파벳마다 781번 건너뛰게 됨
    weight = [781, 156, 31, 6, 1]
    
    for i, w in enumerate(word):
        answer += alpha.index(w) * weight[i]
    
    return answer + len(word)