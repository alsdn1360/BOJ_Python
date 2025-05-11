def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    
    return answer

    # (0, 0) (0, 1) (0, 2) (0, 3) (1, 0) (1, 1) (1, 2) (1, 3)
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
    # 1 2 3 4 2 2 3 4 3 3 3 4 4 4 4 4