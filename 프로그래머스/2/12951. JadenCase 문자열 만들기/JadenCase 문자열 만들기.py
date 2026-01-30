def solution(s):
    answer = []
    
    s_list = list(s.split(' '))
    
    for word in s_list:
        if word:
            answer.append(word.capitalize())
        else:
            answer.append(word)
        
    return ' '.join(answer)