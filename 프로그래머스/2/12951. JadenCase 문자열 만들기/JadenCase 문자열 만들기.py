def solution(s):
    answer = []
    line = s.split(' ')
    
    for l in line:
        answer.append(l.capitalize())
        
    return ' '.join(answer)