import math

def solution(n, k):
    answer = []
    person = [i for i in range(1, n + 1)]
    k -= 1  # 인덱스를 0부터 시작하도록 변환

    for idx in range(n, 0, -1):
        fact = math.factorial(idx - 1)
        
        num_idx = k // fact  # 현재 위치의 인덱스 결정
        
        answer.append(person[num_idx])  # 해당 인덱스의 숫자 추가
        person.pop(num_idx)  # 사용한 숫자 제거
        
        k = k % fact  # k를 남은 순열 블록 내로 이동

    return answer
