def solution(word):
    answer = 0
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    # 그 자리 뒤에 올 수 있는 모든 가능한 단어들의 개수
    # [(5⁰ + 5¹ + 5² + 5³ + 5⁴), (5⁰ + 5¹ + 5² + 5³), ...]
    weight = [781, 156, 31, 6, 1]
    
    for i, w in enumerate(word):
		    # 각 알파벳마다 781번 건너뛰게 되므로 알파벳의 인덱스를 곱해줌
        answer += alpha.index(w) * weight[i]
    
    return answer + len(word)