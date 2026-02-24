from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a,b)


def solution(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    elif n == 2:
        return lcm(arr[0], arr[1])
    else:
        answer = lcm(arr[0], arr[1])
        
        for i in range(2, n):
            answer = lcm(answer, arr[i])
    
        return answer
