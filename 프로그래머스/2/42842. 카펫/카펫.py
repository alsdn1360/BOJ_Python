from itertools import combinations

def check_area(x, y, yellow):
    return True if (x * y) + (-2) * (x + y) + 4 == yellow else False

def solution(brown, yellow):
    area = brown + yellow
    x = area // 3
    y = 3
    
    while x >= y:
        if area % x == 0:
            y = area // x
            
            if check_area(x, y, yellow):
                return [x, y]
        
        x -= 1
        