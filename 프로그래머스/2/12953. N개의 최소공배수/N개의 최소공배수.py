# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a

# 최소공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    answer = 1
    
    n = len(arr)
    
    if n == 1:
        return arr[0]
    else:
        for num in arr:
            answer = lcm(answer, num)
    
    return answer