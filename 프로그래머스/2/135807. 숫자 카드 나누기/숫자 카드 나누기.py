from functools import reduce
from math import gcd

def solution(arrayA, arrayB):
    answer = [0]
    
    # 철수와 영희 카드의 최대공약수 구하기
    gcd_a = reduce(gcd, arrayA)
    gcd_b = reduce(gcd, arrayB)
    
    is_a = True
    is_b = True
    
    # 조건 1 체크
    for num_b in arrayB:
        if num_b % gcd_a == 0:
            is_a = False
            break
            
    # 조건 2 체크
    for num_a in arrayA:
        if num_a % gcd_b == 0:
            is_b = False
            break
    
    if is_a:
        answer.append(gcd_a)
    
    if is_b:
        answer.append(gcd_b)
        
    return max(answer)