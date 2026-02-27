def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n1, n2, n3 = len(p1), len(p2), len(p3)
    cnt = [0] * 3
    
    for i, ans in enumerate(answers):
        if ans == p1[i % n1]:
            cnt[0] += 1
        if ans == p2[i % n2]:
            cnt[1] += 1
        if ans == p3[i % n3]:
            cnt[2] += 1
            
    max_cnt = max(cnt)
    
    for i, c in enumerate(cnt):
        if max_cnt == c:
            answer.append(i + 1)
    
    return answer