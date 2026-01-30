def solution(s):
    answer = []
    
    s_list = list(s.split(' '))
    
    for word in s_list:
        if not word:
            answer.append(word)
            
            continue
            
        lower_word = word.lower()
        jaden_word = lower_word[0].upper() + lower_word[1:]
        
        answer.append(jaden_word)
        
    return ' '.join(answer)