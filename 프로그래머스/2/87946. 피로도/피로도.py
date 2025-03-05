def dfs(k, dungeons, visited, cnt):
    max_cnt = cnt
    
    for i, (min_fati, use_fati) in enumerate(dungeons):
        if not visited[i] and k >= min_fati:
            visited[i] = True
            
            max_cnt = max(max_cnt, dfs(k - use_fati, dungeons, visited, cnt + 1))
            
            visited[i] = False
            
    return max_cnt

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    return dfs(k, dungeons, visited, 0)
    
        