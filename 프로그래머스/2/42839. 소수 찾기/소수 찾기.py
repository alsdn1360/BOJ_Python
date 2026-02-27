from itertools import permutations
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    answer = 0
    n = len(numbers)
    
    papers = list(numbers)
    
    made_nums = set()
    
    for i in range(1, n + 1):
        for permu in permutations(papers, i):
            made_nums.add(int(''.join(permu)))
    
    for made_num in made_nums:
        if is_prime(made_num):
            answer += 1
            
    return answer