from collections import deque, defaultdict

def solution(n, wires):
    answer = []
    
    # 간선을 하나씩 뛰어넘어가면서 연결 요소 수를 세기 위함
    for step in range(n - 1):
        tree = defaultdict(list)
        
        # 해당하는 간선은 제외하고 tree에 넣음
        for i, (v1, v2) in enumerate(wires):
            if step == i:
                continue
                
            tree[v1].append(v2)
            tree[v2].append(v1)
            
        # 전부 연결되어 있으니 시작은 1부터
        queue = deque([1])
        visited = set()
        visited.add(1)
        
        tower_cnt = 1
        
        while queue:
            curr_tower = queue.popleft()
            
            for adj_tower in tree[curr_tower]:
                if adj_tower not in visited:
                    queue.append(adj_tower)
                    visited.add(adj_tower)
                    tower_cnt += 1
                 
        # (n - tower_cnt)에서 또 tower_cnt를 빼줘야 함 
        answer.append(abs(n - (2 * tower_cnt)))
        
    return min(answer)