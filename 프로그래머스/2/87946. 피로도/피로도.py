def bt(n, k, dungeons, cnt, visited):
    global answer
    
    answer = max(answer, cnt)
    
    for i, (need_fatigue, fatigue) in enumerate(dungeons):
        if not visited[i] and k >= need_fatigue:
            visited[i] = True
            k -= fatigue
            cnt += 1
        
            bt(n, k, dungeons, cnt, visited)

            cnt -= 1
            k += fatigue
            visited[i] = False
        

def solution(k, dungeons):
    global answer
    answer = -1
    
    n = len(dungeons)
    
    dungeons.sort(key = lambda x : (-x[0], x[1]))
    visited = [False] * n
    
    bt(n, k, dungeons, 0, visited)
    
    return answer