def solution(enroll, referral, seller, amount):
    # 트리에서 부모가 누구인지 나타내는 딕셔너리
    parent = dict(zip(enroll, referral))
    
    # 각자 얼마를 벌었는지 구하는 딕셔너리
    total_amount = {name : 0 for name in enroll}
    
    for i in range(len(seller)):
        # 판매한 사람과 수익금
        curr_seller = seller[i]
        earn = amount[i] * 100
        
        # 센터가 나올 때까지 위로 올라가면서 수익금 분배
        while earn > 0 and curr_seller != '-':
            # 현재 판매자가 가져가는 수익금
            total_amount[curr_seller] += earn - (earn // 10)
            curr_seller = parent[curr_seller]
            
            # 추천자에게 가는 금액
            earn //= 10
            
    return [total_amount[name] for name in enroll]