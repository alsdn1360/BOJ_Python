def check_same_area(arr, x, y, size):
    prev_num = arr[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if prev_num != arr[i][j]:
                return False
            
    return True

def divide_quad(arr, answer, x, y, size):
    if size == 1:
        # 현재 영역의 크기가 1이면 그 값 개수 추가
        answer[arr[x][y]] += 1
        return
    
    if check_same_area(arr, x, y, size):
        # 압축시킨 후, 현재 값 개수 추가
        answer[arr[x][y]] += 1
        return
    else:
        resize = size // 2
        
        # 4개의 영역으로 쪼갬
        divide_quad(arr, answer, x, y, resize)
        divide_quad(arr, answer, x + resize, y, resize)
        divide_quad(arr, answer, x, y + resize, resize)
        divide_quad(arr, answer, x + resize, y + resize, resize)

def solution(arr):
    answer = [0, 0]
    
    divide_quad(arr, answer, 0, 0, len(arr))
    
    return answer
