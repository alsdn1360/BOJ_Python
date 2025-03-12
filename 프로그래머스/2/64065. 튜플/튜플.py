def solution(s):
    answer = []
    
    # s에서 맨 앞 {{와 맨 뒤 }}를 제거하기 위함
    s = s[2 : -2].split('},{')
    s.sort(key = len)
    
    # s의 항목들을 하나씩 가져옴
    for num_list in s:
        # 가져온 항목 들을 하나씩 분리함
        nums = num_list.split(',')
        
        for elem in nums:
            # 정답이 정수이므로 정수로 변환
            target = int(elem)
            
            # 중복되는 값이므로 answer에 없으면 삽입
            if target not in answer:
                answer.append(target)
                
    return answer