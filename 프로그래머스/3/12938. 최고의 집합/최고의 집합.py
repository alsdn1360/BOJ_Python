'''
1. 여러 개의 수 중에서 그 수 들의 차이가 작을수록 곱은 커짐
2. 그렇게 되려면 s를 n으로 나누고나서 뒤에 숫자들을 구하면 되지 않을까? (s // n)
'''

def solution(n, s):
    answer = []
    
    while n > 0:
        num = s // n
        
        # 몫이 1보다 작으면 자연수 합을 구할 수 없음
        if num < 1:
            break
        else:   
            answer.append(num)
            s -= num
            n -= 1
    
    return sorted(answer) if len(answer) > 0 else [-1]