from collections import defaultdict

def solution(nums):    
    return min(len(nums) / 2, len(set(nums)))