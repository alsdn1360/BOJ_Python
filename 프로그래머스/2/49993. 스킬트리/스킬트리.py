def solution(skill, skill_trees):
    answer = 0
    
    # 스킬트리를 리스트로 변환
    skill_trees = [list(st) for st in skill_trees]
    
    for skill_tree in skill_trees:
        idx = 0 # 스킬의 순서 인덱스
        able = True # 스킬트리 가능 여부
        
        for s in skill_tree:
            if s not in skill:
                continue
                
            # 배워야할 스킬의 순서가 아닐 때
            if s != skill[idx]:
                able = False
                break
                
            idx += 1
            
        if able:
            answer += 1
            
    return answer