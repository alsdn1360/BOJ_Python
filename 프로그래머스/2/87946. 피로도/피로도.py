def backtrack(k, dungeons, visited):
    max_cnt = 0
    
    for i, (min_f, use_f) in enumerate(dungeons):
        if not visited[i] and k >= min_f:
            visited[i] = True
            
            max_cnt = max(max_cnt, backtrack(k - use_f, dungeons, visited) + 1)
            
            visited[i] = False
            
    return max_cnt


def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    return backtrack(k, dungeons, visited)
