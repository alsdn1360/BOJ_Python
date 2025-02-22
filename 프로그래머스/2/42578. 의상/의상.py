def solution(clothes):
    answer = 1
    closet = {}
    
    for cloth, category in clothes:
        # 카테고리별로 가지고 있는 옷의 개수를 셈
        # 해당되는 카테고리가 없으면 0으로 초기화한 뒤 1을 더하고, 있으면 거기에 1을 더함
        closet[category] = closet.get(category, 0) + 1
        
    # 카테고리별로 가지고 있는 옷의 개수를 전부 곱함
    # 여기서 입지 않은 경우의 수도 있으니 +1을 해줌
    for cnt in closet.values():
        answer *= (cnt + 1)
    
    # 아무것도 선택하지 않은 경우가 포함되어 있으니 -1을 해줌
    return answer - 1
        
        