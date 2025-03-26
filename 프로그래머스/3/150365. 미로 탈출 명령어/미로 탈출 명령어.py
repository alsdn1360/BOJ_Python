from collections import deque
import sys

sys.setrecursionlimit(10**6)

# d, l, r, u 순으로 이동하면 사전순으로 이동
MOVES = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

# 격자의 시작 지점이 좌상단이 (1, 1)이므로 1부터 시작
def oob(n, m, nx, ny):
    return 1 <= nx <= n and 1 <= ny <= m
    
def dfs(n, m, curr_x, curr_y, r, c, path, remaining_move, answer):
    # 정답이 나왔으면 더 이상 탐색 안함
    if answer:
        return
    
    # 맨해튼 거리로 현재 거리로부터 최소거리 측정
    min_remaining = abs(r - curr_x) + abs(c - curr_y)
    
    if min_remaining > remaining_move or (remaining_move - min_remaining) % 2 != 0:
        return
    
    # 탈출 지점에 도착했으면 answer에 삽입
    if curr_x == r and curr_y == c and remaining_move == 0:
        answer.append(path)
        return
    
    for dirc, dx, dy in MOVES:
        nx, ny = curr_x + dx, curr_y + dy
        
        if oob(n, m, nx, ny):
            dfs(n, m, nx, ny, r, c, path + dirc, remaining_move - 1, answer)
    
def solution(n, m, x, y, r, c, k):
    answer = []
    
    # 맨해튼 거리로 시작 지점으로부터 최소거리 측정
    min_distance = abs(r - x) + abs(c - y)
    
    # k보다 최소 거리가 크면 갈 수 없음
    # k - min_distance가 짝수여야 제자리에서 왔다갔다하는 경우도 할 수 있음
    if min_distance > k or (k - min_distance) % 2 != 0:
        return 'impossible'
    
    dfs(n, m, x, y, r, c, '', k, answer)
    
    return answer[0] if answer else 'impossible'