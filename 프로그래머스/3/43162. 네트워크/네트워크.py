from collections import defaultdict

def dfs(adj_list, curr_computer, visited):
    # 현재 컴퓨터 방문 처리
    visited.add(curr_computer)
    
    # 현재 컴퓨터에 인접한 컴퓨터 불러오기
    for adj_computer in adj_list[curr_computer]:
        # 그 중에서 방문하지 않은 컴퓨터면 dfs 실행
        if adj_computer not in visited:
            dfs(adj_list, adj_computer, visited)

def solution(n, computers):
    answer = 0

    # 각 컴퓨터와 연결된 인접한 컴퓨터 리스트
    adj_list = defaultdict(list)
    # 방문한 컴퓨터 초기화
    visited = set()
    
    # computers 중에서 1이면 연결이 되어있으므로 현재 컴퓨터와 연결
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
                
    # 아직 방문하지 않은 컴퓨터는 연결되어 있지 않은 것이므로 네트워크 +1, 이후 그 컴퓨터에 대한 dfs 실행
    for i in range(n):
        if i not in visited:
            answer += 1
            dfs(adj_list, i, visited)
                
    return answer