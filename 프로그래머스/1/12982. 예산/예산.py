def solution(d, budget):
    answer = 0
    
    d.sort()
    n = len(d)
    
    for i in range(n):
        temp_budget = budget
        cnt = 0
            
        # 첫 번째 값이 budget보다 작거나 같아야 빼고 cnt +1
        if budget >= d[i]:
            temp_budget -= d[i]
            cnt += 1
        
        # 그 다음 값부터 계속 빼면서 0보다 크면 cnt +1
        for j in range(i + 1, n):
            if temp_budget - d[j] >= 0:
                temp_budget -= d[j]
                cnt += 1
                
        # 이전의 최대값이랑 지금의 카운트 중에 큰 값으로 갱신
        answer = max(answer, cnt)
                
    return answer