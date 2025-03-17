from collections import Counter

def solution(topping):
    answer = 0
    
    # 토핑의 종류는 중복되면 안되므로, 철수는 set
    # 처음에는 동생이 모든 토핑을 가지고 있는 것으로 간주하고, 토핑의 종류를 셈
    chulsoo = set()
    bro = Counter(topping)
    
    for curr_topping in topping:
        # 현재 토핑을 철수에게 하나 씩 건네줌
        chulsoo.add(curr_topping)
        bro[curr_topping] -= 1
        
        if bro[curr_topping] == 0:
            del bro[curr_topping]
            
        if len(chulsoo) == len(bro):
            answer += 1
            
    return answer