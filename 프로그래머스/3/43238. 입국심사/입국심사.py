# 이진탐색으로 해결
def binary_search(n, low, high, times):
    # 가장 작은 값이 큰 값보다 커지면 탐색 종료
    if low > high:
        return low
    
    sum = 0
    mid = (low + high) // 2
    
    for t in times:
        sum += mid // t
    
    # 합이 n보다 크거나 같으면 시간이 충분하니까 최대값을 줄임
    if sum >= n:
        return binary_search(n, low, mid - 1, times)
    # 합이 n보다 작으면 시간이 부족하니까 최소값을 늘림
    elif sum < n:
        return binary_search(n, mid + 1, high, times)

def solution(n, times):    
    return binary_search(n, 1, n * min(times), times)
