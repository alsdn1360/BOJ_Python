from collections import defaultdict


def solution(message, spoiler_ranges):
    answer = 0
    
    n = len(message)
    
    all_words_idx = []
    word = ''
    s_idx = 0
    
    for i, c in enumerate(message):
        if c == ' ':
            all_words_idx.append([word, s_idx, i - 1])
            word = ''
            s_idx = i + 1
        else: 
            word += c
            
    all_words_idx.append([word, s_idx, n - 1])
    
    non_spoiler_words = set()
    spoiler_words = []
    
    idx = 0
    
    for word, s_idx, e_idx in all_words_idx:
        is_spoiled = False
        
        for spoiler_s_idx, spoiler_e_idx in spoiler_ranges:
            if s_idx <= spoiler_e_idx and e_idx >= spoiler_s_idx:
                is_spoiled = True
                break
                
        if is_spoiled:
            spoiler_words.append(word)
        else:
            non_spoiler_words.add(word)
        
    opend_words = set()
    
    for spoiler_word in spoiler_words:
        if spoiler_word in non_spoiler_words:
            continue
            
        if spoiler_word in opend_words:
            continue
            
        answer += 1
        opend_words.add(spoiler_word)

    return answer
