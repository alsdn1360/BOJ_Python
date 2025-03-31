def dfs(idx, numbers, target, total):
    if idx == len(numbers):
        return 1 if total == target else 0

    # 양수로 더하는 경우랑 음수로 더하는 경우를 dfs에 둘 다 넣어서 계산함
    return dfs(idx + 1, numbers, target, total + numbers[idx]) + dfs(idx + 1, numbers, target, total - numbers[idx])
            
def solution(numbers, target):
    return dfs(0, numbers, target, 0)