def solution(s):
    arr = sorted(list(map(int, s.split())))
    
    return str(arr[0]) + ' ' + str(arr[-1])