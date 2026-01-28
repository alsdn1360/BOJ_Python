def solution(s):
    num_s = sorted(list(map(int, s.split(' '))))
    
    return f"{num_s[0]} {num_s[-1]}"
    