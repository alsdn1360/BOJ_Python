from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for c in course:
        course_menu = []
        
        for order in orders:
            # 코스 메뉴 개수에 따라서 조합을 만들어서 메뉴 리스트에 추가함
            candidate = combinations(sorted(order), c)
            course_menu += candidate
            
            # 각 조합의 개수를 구함
            # Counter를 사용하면 딕셔너리로 key는 항목, value는 그 항목의 개수가 저장됨
            count = Counter(course_menu)
            
        # 가장 많이 나온 조합이 최소 2명 이상의 손님으로부터 주문되어야 함
        if (len(count) != 0 and max(count.values()) >= 2):
            for menu, cnt in count.items():
                # 가장 많이 주문된 조합이면 추가
                if cnt == max(count.values()):
                    result.append("".join(menu))
                        
    return sorted(result)
