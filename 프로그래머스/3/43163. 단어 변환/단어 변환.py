def check_diff_one(word1, word2):
    diff_cnt = 0
    
    for (c1, c2) in zip(word1, word2):
        if c1 != c2:
            diff_cnt += 1
            
        if diff_cnt > 1:
            return False
            
    return True if diff_cnt == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = float('inf')
    n = len(words)
    
    visited = [False] * n
    
    def dfs(visited, curr_word, cnt):
        nonlocal answer
        
        if curr_word == target:
            return cnt
        
        for i, word in enumerate(words):
            if check_diff_one(curr_word, word) and not visited[i]:
                visited[i] = True
                
                answer = min(answer, dfs(visited, word, cnt + 1))
                
                visited[i] = False
                
        return answer
        
    return dfs(visited, begin, 0)
