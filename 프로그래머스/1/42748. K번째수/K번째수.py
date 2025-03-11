def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        temp_arr = array[i - 1 : j]
        temp_arr.sort()
        
        answer.append(temp_arr[k - 1])
        
    return answer