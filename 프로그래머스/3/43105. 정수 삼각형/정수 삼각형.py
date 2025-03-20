def solution(triangle):
    answer = 0
    
    # triangle의 각 행마다 처음과 끝에 0을 더함
    # [i - 1][j - 1]과 [i - 1][j]의 값을 더하기 위함
    triangle = [[0] + row + [0] for row in triangle]
    
    for i in range(1, len(triangle)):
        # 마지막에 0을 더한 부분에서 [i - 1][j]를 하면 인덱스 에러가 발생하기 때문에 -1
        for j in range(1, len(triangle[i]) - 1):
            # [i - 1][j - 1]과 [i - 1][j]의 값을 더한 값 중에 더 큰 값을 넣음
            triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])
            
            # 현재까지 최대값과 지금의 값을 비교
            answer = max(answer, triangle[i][j])
            
    return answer