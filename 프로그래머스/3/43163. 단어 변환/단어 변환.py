from collections import deque

# 알파벳이 하나만 다른 단어 찾기
def is_different(word1, word2):
    cnt = 0
    
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            cnt += 1
            
    return cnt == 1

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        curr_word, step = queue.popleft()
        
        if curr_word == target:
            return step
        
        for word in words:
            if word not in visited and is_different(curr_word, word):
                visited.add(word)
                queue.append((word, step + 1))
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)