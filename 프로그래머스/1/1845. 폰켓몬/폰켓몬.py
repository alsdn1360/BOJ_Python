def solution(nums):
    N = len(nums)
    
    # 중복을 제거하면 폰켓몬 종류만 남음
    ponkemon = set(nums)
    
    # N / 2마리랑 종류의 개수 중에 더 작은 값 고르면 됨
    return min(N / 2, len(ponkemon))
    