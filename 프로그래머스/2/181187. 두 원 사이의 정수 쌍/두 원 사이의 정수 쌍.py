import math

def solution(r1, r2):
    answer = 0
    
    for x in range(0, r2 + 1):
        # r1^2 - x^2 <= y^2 <= r2^2 - x^2 공식을 이용해서 갯수를 셈
        min_y = math.ceil(math.sqrt(max(0, r1*r1 - x*x)))
        max_y = math.floor(math.sqrt(r2*r2 - x*x))
        
        if min_y > max_y:
            continue
        
        # 둘 다 0이 아니면 4배, x나 y 중 0이 있으면 2배
        if x == 0:
            answer += 2 * (max_y - min_y + 1)
        else:
            if min_y == 0:
                # (x, 0) (-x, 0) 두 가지 경우의 수 추가
                answer += 4 * max_y + 2
            else:
                # y가 전부 양수일 때
                answer += 4 * (max_y - min_y + 1)

    return answer
