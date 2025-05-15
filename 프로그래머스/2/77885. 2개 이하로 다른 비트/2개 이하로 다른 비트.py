def solution(numbers):
    answer = []
    
    for num in numbers:
        # 짝수는 첫 비트가 항상 0이므로, 다음 숫자의 다른 비트의 개수가 항상 1개임
        if num % 2 == 0:
            answer.append(num + 1)
        # 홀수는 첫 비트가 항상 1
        else:
            target = format(num, 'b')
            
            # 비트 중에 0이 없으면 만들어줘야 함
            if '0' not in target:
                target = '0' + target
                
            # 가장 오른쪽에 있는 0 비트를 찾음
            first_zero = target.rfind('0')
                
            target = list(target)
            
            # 그 0 비트를 1로 만들고, 그 오른쪽의 비트를 0으로 만들면 항상 2개 차이남
            target[first_zero] = '1'
            target[first_zero + 1] = '0'
            
            answer.append(int(''.join(target), 2))
    
    return answer