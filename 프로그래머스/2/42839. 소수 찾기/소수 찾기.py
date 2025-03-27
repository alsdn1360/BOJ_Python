from itertools import permutations

# 소수 판별
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    
    # 겹치는 숫자 없이
    combi = set()
    
    # 종이 조각을 이용해서 만들 수 있는 모든 숫자 순열
    for i in range(1, len(numbers) + 1):
        for comb in permutations(numbers, i):
            combi.add(int(''.join(comb)))
            
    for num in combi:
        if is_prime(num):
            answer += 1
    
    return answer