def solution(arr1, arr2):
    # 각 행렬의 크기
    r1, c1 = len(arr1), len(arr1[0]) # 3 , 2
    r2, c2 = len(arr2), len(arr2[0]) # 2 , 2
    
    # 결과 행렬의 크기
    answer = [[0] * c2 for _ in range(r1)] # 3 , 2
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer
