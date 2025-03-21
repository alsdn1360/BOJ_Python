from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # 귤의 종류 별 개수를 세서 많은 것 부터 내림차순으로 리스트를 만듦
    tangerine_cnt = Counter(tangerine).most_common()
    n = len(tangerine_cnt)
    
    for i in range(n):
        if k <= 0:
            break
        
        # 귤 종류의 개수가 많은 것부터 빼줌
        k -= tangerine_cnt[i][1]
        answer += 1
    
    return answer