def solution(want, number, discount):
    dic = {}
    
    n = len(want)
    
    # 딕셔너리에 원하는 품목을 키 값으로, 원하는 수를 밸류로 지정
    for i in range(n):
        dic[want[i]] = number[i]
        
    result = 0
    
    # 일별 할인 제품 체크
    for i in range(len(discount) - 9):
        discount_dic = {}
        
        # 일별 할인 제품을 새로운 딕셔너리에 넣기
        for d in discount[i : i + 10]:
            if d in dic:
                discount_dic[d] = discount_dic.get(d, 0) + 1
                
        # 두 개의 딕셔너리가 같아야 회원 가입 할 날짜임
        if dic == discount_dic:
            result += 1
            
    return result