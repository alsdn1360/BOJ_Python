from collections import defaultdict

def solution(phone_book):
    numbers = defaultdict(bool)
    
    for p_b in phone_book:
        numbers[p_b] = True
        
    for number in phone_book:
        n = len(number)
        
        for i in range(n):
            if numbers[number[:i]]:
                return False

    return True