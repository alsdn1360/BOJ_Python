def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        # 현재 스킬트리에서 스킬에 속하는 부분만 추출
        filtered_skill_tree = ''.join([s for s in skill_tree if s in skill])
        
        if filtered_skill_tree == skill[:len(filtered_skill_tree)]:
            answer += 1
            
    return answer